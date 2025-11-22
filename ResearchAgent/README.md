# Research Agent - Assignment

A simple research agent built with Pydantic-AI that has tool calls and Logfire logging.

## What It Does

This agent can:
- 🔍 Search for information
- 🧮 Do math calculations  
- 📊 Analyze data
- 📅 Tell you the date/time
- 📚 Answer questions about programming topics

## Setup (3 Steps)

### 1. Install Dependencies

```bash
pip3 install pydantic-ai logfire google-generativeai requests python-dotenv
```

### 2. Get API Keys

**Gemini API Key** (free):
- Go to: https://makersuite.google.com/app/apikey
- Click "Create API Key"
- Copy it

**Logfire Token** (free):
- Go to: https://logfire.pydantic.dev/
- Sign up
- Create a project
- Copy the write token

### 3. Create .env File

Create a file called `.env` in this folder and add:

```
GEMINI_API_KEY=paste_your_key_here
LOGFIRE_TOKEN=paste_your_token_here
```

## How to Run

```bash
python3 research_agent.py
```

Then type your questions! For example:
- "Search for information about Python"
- "Calculate 25 * 4 + 100"
- "Analyze this data: 45, 67, 89, 72, 55"
- "What is today's date?"

Type `quit` to exit.

## View Logs

Go to https://logfire.pydantic.dev/ to see all the LLM calls and tool usage.

## Assignment Requirements ✅

- ✅ Research Agent with Pydantic-AI
- ✅ Tool calls (5 tools)
- ✅ Logfire instrumentation
- ✅ Sample execution logs in Logfire

---

That's it! Simple research agent for your assignment.










