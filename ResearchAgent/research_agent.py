import os
import requests
from collections import Counter
import difflib
from datetime import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import json


load_dotenv()

def majority_answer(findings):
    """
    Compare the answers in the findings, determine the majority answer,
    and provide a confidence percentage.
    Returns: (majority_answer, confidence_percent, answer_counts)
    """
    # Normalize summaries for comparison (lowercase, strip, remove trailing ...)
    def normalize(text):
        return (text or "").lower().strip().rstrip("...")

    # Combine title and summary for more comprehensive comparison
    normalized = [
        normalize(f.get("title", "") + " " + f.get("summary", ""))
        for f in findings
        if f.get("title") or f.get("summary")
    ]
    if not normalized:
        return ("", 0.0, {}, [])

    # Fuzzy grouping: group answers that are similar
    # Use both sequence matching and token overlap for better semantic comparison
    def similarity_score(text1, text2):
        """Calculate similarity using both sequence matching and token overlap."""
        # Sequence similarity
        seq_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()

        # Token overlap (Jaccard similarity)
        tokens1 = set(text1.split())
        tokens2 = set(text2.split())
        if not tokens1 or not tokens2:
            return seq_ratio
        intersection = len(tokens1 & tokens2)
        union = len(tokens1 | tokens2)
        token_ratio = intersection / union if union > 0 else 0

        # Combine both metrics (weighted average favoring token overlap for semantic similarity)
        return 0.3 * seq_ratio + 0.7 * token_ratio

    groups = []  # Each group is a list of indices
    used = set()
    for i, ans in enumerate(normalized):
        if i in used:
            continue
        group = [i]
        used.add(i)
        for j in range(i+1, len(normalized)):
            if j in used:
                continue
            if similarity_score(ans, normalized[j]) > 0.3:
                group.append(j)
                used.add(j)
        groups.append(group)

    # Find the largest group
    majority_group = max(groups, key=len)
    freq = len(majority_group)
    # Return the summary (not title+summary) for display, but confidence is based on title+summary comparison
    majority = normalize(findings[majority_group[0]].get("summary", "")) if majority_group else ""
    confidence = freq / len(normalized)
    evidence_indices = majority_group
    # For reporting, build a fuzzy count dictionary
    fuzzy_counts = {normalized[i]: len([idx for idx in majority_group if normalized[idx] == normalized[i]]) for i in majority_group}
    return (majority, confidence, fuzzy_counts, evidence_indices)




# SerpAPI for Google Search
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"


def serpapi_search(query, num_results=3):
    """Search using SerpAPI Google Search and return top results."""
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": num_results
    }
    resp = requests.get(SERPAPI_ENDPOINT, params=params)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("organic_results", [])[:num_results]:
        results.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet", ""),
        })
    return results

def extract_content(url):
    """Extract title, top paragraph, and date from a web page."""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.title.string.strip() if soup.title else ""
        # Find the first non-empty paragraph
        paragraphs = [p.get_text().strip() for p in soup.find_all("p") if p.get_text().strip()]
        top_paragraph = paragraphs[0] if paragraphs else ""
        # Try to find a date
        date = ""
        for meta in soup.find_all("meta"):
            if meta.get("property", "").lower() in ["article:published_time", "og:published_time"] or meta.get("name", "").lower() in ["pubdate", "publishdate", "date", "dc.date"]:
                date = meta.get("content", "")
                break
        return {"title": title, "top_paragraph": top_paragraph, "date": date}
    except Exception as e:
        return {"title": "", "top_paragraph": "", "date": "", "error": str(e)}

def research_agent(question):
    """Main research agent logic."""
    search_results = serpapi_search(question)
    findings = []
    sources_structured = []
    # Assign source ids
    for idx, result in enumerate(search_results):
        url = result["link"]
        extracted = extract_content(url)
        source_id = f"s{idx+1}"
        findings.append({
            "title": extracted["title"] or result["title"],
            "summary": extracted["top_paragraph"] or result["snippet"],
            "date": extracted["date"],
            "url": url,
            "source_id": source_id,
            "snippet": result["snippet"]
        })
        # Try to parse date to YYYY-MM-DD
        published = ""
        if extracted["date"]:
            try:
                published = str(datetime.fromisoformat(extracted["date"]).date())
            except Exception:
                published = extracted["date"]
        sources_structured.append({
            "id": source_id,
            "title": extracted["title"] or result["title"],
            "url": url,
            "snippet": result["snippet"],
            "published": published
        })

    # Majority answer logic
    majority, confidence, answer_counts, evidence_indices = majority_answer(findings[:3]) if findings else ("", 0.0, {}, [])
    # Compose key_findings
    key_findings = []
    if majority:
        evidence = [findings[i]["source_id"] for i in evidence_indices]
        key_findings.append({
            "finding": majority,
            "evidence": evidence,
            "confidence": round(confidence, 2)
        })

    # Compose summary (short answer)
    summary = majority if majority else (findings[0]["summary"] if findings else "")

    # Compose output in requested format
    output = {
        "query": question,
        "summary": summary,
        "key_findings": key_findings,
        "confidence": round(confidence, 2) if majority else 0.0,
        "sources": sources_structured,
        "findings": findings,  # Add findings for downstream use
        "raw_tool_outputs": {
            "serpapi": search_results,
            "bing": ""
        }
    }
    return output

if __name__ == "__main__":
    print("Welcome to the Research Agent! Type your question and get structured answers. Type 'exit' to quit.") 
    while True:
        question = input("\nEnter your research question: ").strip()
        if question.lower() in ("exit", "quit"): break
        print("\nResearching...\n")
        result = research_agent(question)

        # Print concise top 3 findings if available
        if result.get("findings") and len(result["findings"]):

            print("\nTop 3 Findings:\n")
            for i, finding in enumerate(result["findings"][:3], 1):
                print(f"{i}. {finding['title']}\n")
                print(f"   {finding['summary']}\n")
                print(f"   [Read more]({finding['url']})\n")


            # Toolcall: Compare answers and give majority solution with confidence

            majority, confidence, answer_counts, evidence_indices = majority_answer(result["findings"][:3])

            if majority:
                print("\nMajority Solution:\n")
                # Print each sentence or phrase on a new line for clarity
                for line in majority.split(';'):
                    line = line.strip()
                    if line:
                        print(line)
                print(f"\nConfidence: {confidence}% \n\n")
            else:
                print("No clear majority answer found.\n\n")
        else:
            print("\nNo findings available for this query.\n")
