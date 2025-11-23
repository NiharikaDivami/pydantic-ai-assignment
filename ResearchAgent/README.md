# Research Agent

An intelligent research agent that searches the web, extracts information from multiple sources, and provides consensus-based answers with confidence scores. Built with Python, SerpAPI, and BeautifulSoup.

## Features

- **Multi-Source Research**: Searches Google via SerpAPI and extracts content from top results
- **Content Extraction**: Scrapes web pages for titles, paragraphs, and publication dates
- **Consensus Analysis**: Compares answers from multiple sources using fuzzy matching
- **Confidence Scoring**: Provides confidence percentages based on source agreement
- **Structured Output**: Returns organized findings with citations and evidence
- **CLI Interface**: Interactive command-line interface for asking research questions

## How It Works

1. **Search**: Queries Google using SerpAPI to get top 3 results
2. **Extract**: Scrapes each result page for detailed content
3. **Analyze**: Compares answers using semantic similarity (sequence matching + token overlap)
4. **Synthesize**: Identifies majority consensus and calculates confidence
5. **Present**: Shows top findings with sources and confidence scores

## Prerequisites

- Python 3.10 or higher
- SerpAPI account (for Google search)

## Installation

### 1. Clone and Navigate

```bash
cd /Users/niharika/Documents/GitClones/pydantic-ai-assignment/ResearchAgent
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install requests beautifulsoup4 python-dotenv
```

Or using the project file:

```bash
pip install -e .
```

### 4. Get SerpAPI Key

1. Go to: https://serpapi.com/
2. Sign up for a free account (100 searches/month free)
3. Copy your API key from the dashboard

### 5. Configure Environment

Create or update the `.env` file:

```bash
SERPAPI_KEY=your_serpapi_key_here
```

## Usage

### Start the Research Agent

```bash
python research_agent.py
```

### Example Questions

```
Enter your research question: What is the capital of France?

Researching...

Top 3 Findings:

1. Paris - Wikipedia
   Paris is the capital and largest city of France...
   [Read more](https://en.wikipedia.org/wiki/Paris)

2. Capital of France - Britannica
   Paris, city and capital of France, located in the north-central...
   [Read more](https://www.britannica.com/place/Paris)

3. Paris Facts - National Geographic
   Paris is the capital of France and one of Europe's major centres...
   [Read more](https://www.nationalgeographic.com/travel/article/paris)

Majority Solution:
Paris is the capital and largest city of France

Confidence: 100%
```

### More Example Queries

- "What are the health benefits of green tea?"
- "How does photosynthesis work?"
- "What is quantum computing?"
- "Latest developments in artificial intelligence"

Type `exit` or `quit` to stop the agent.

## Output Structure

The agent returns a structured dictionary with:

```python
{
    "query": "Your question",
    "summary": "Short consensus answer",
    "key_findings": [
        {
            "finding": "Main insight",
            "evidence": ["s1", "s2"],  # Source IDs
            "confidence": 0.85
        }
    ],
    "confidence": 0.85,
    "sources": [
        {
            "id": "s1",
            "title": "Article Title",
            "url": "https://...",
            "snippet": "Preview text",
            "published": "2024-01-15"
        }
    ],
    "findings": [...],  # Detailed findings
    "raw_tool_outputs": {...}  # Raw API responses
}
```

## How Consensus Works

The agent uses a sophisticated similarity algorithm:

1. **Normalization**: Converts text to lowercase and strips whitespace
2. **Sequence Matching**: Compares character sequences (30% weight)
3. **Token Overlap**: Calculates Jaccard similarity on word tokens (70% weight)
4. **Grouping**: Groups similar answers (>30% similarity threshold)
5. **Majority**: Identifies the largest group as consensus
6. **Confidence**: Percentage = (majority_count / total_sources)

## Project Structure

```
ResearchAgent/
├── research_agent.py    # Main agent implementation
├── pyproject.toml       # Project dependencies
├── .env                 # API keys (DO NOT COMMIT)
├── .gitignore          # Git ignore rules
├── .venv/              # Virtual environment
├── .logfire/           # Logfire logs
└── README.md           # This file
```

## Key Functions

### `serpapi_search(query, num_results=3)`
Searches Google and returns top results with titles, links, and snippets.

### `extract_content(url)`
Scrapes a webpage for:
- Page title
- First meaningful paragraph
- Publication date (from meta tags)

### `majority_answer(findings)`
Analyzes findings to determine:
- Majority consensus answer
- Confidence percentage
- Supporting evidence indices

### `research_agent(question)`
Main orchestrator that:
1. Searches for the question
2. Extracts content from results
3. Analyzes for consensus
4. Returns structured output

## Troubleshooting

### "SERPAPI_KEY not found" Error
- Make sure `.env` file exists in the ResearchAgent directory
- Verify the API key is correct
- Check that `python-dotenv` is installed

### "Too Many Requests" Error
- You've exceeded SerpAPI's free tier limit (100/month)
- Wait for the limit to reset or upgrade your plan

### No Results Returned
- Check your internet connection
- Verify the query is in English
- Try a more specific question

### Content Extraction Fails
- Some websites block scraping
- The agent will fall back to using search snippets
- Try different search queries

## Security

- **Never commit `.env`** to version control
- The `.gitignore` file prevents this
- Rotate API keys if accidentally exposed
- Monitor SerpAPI usage to prevent abuse

## Limitations

- Free SerpAPI tier: 100 searches/month
- Some websites block web scraping
- Confidence scores are based on similarity, not factual accuracy
- Results depend on Google search quality
- Limited to top 3 search results

## Future Enhancements

- [ ] Support for more search engines (Bing, DuckDuckGo)
- [ ] Fact-checking against trusted sources
- [ ] Citation formatting (APA, MLA)
- [ ] Export results to JSON/CSV
- [ ] Web UI with search history
- [ ] Caching to reduce API calls

## License

Educational use only.

## Support

For issues:
1. Check your SERPAPI_KEY is valid
2. Verify all dependencies are installed
3. Ensure Python 3.10+ is being used
4. Check internet connectivity

---

**Built for web research with intelligent consensus analysis**










