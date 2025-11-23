# PydanticAI Assignment - Intelligent Agents Collection

A collection of AI-powered applications demonstrating the capabilities of PydanticAI, including an e-commerce shopping assistant and a web research agent.

## 📁 Projects Overview

This repository contains two main projects:

### 1. **E-Commerce Shopping Assistant** (`/Ecommerce`)
An AI-powered shopping assistant with a beautiful web interface built using PydanticAI, FastHTML, and Google Gemini.

**Features:**
-  Natural language cart management
-  Modern gradient UI with smooth animations
-  12 product catalog with quick-add buttons
-  AI agent with tool calling (add, remove, show, clear cart)
-  Real-time chat interface
- 🎯 Smart quantity management

**Tech Stack:** PydanticAI, FastHTML, Google Gemini 2.5 Flash, HTMX, Python

[➡️ View E-Commerce Assistant README](./Ecommerce/README.md)

---

### 2. **Research Agent** (`/ResearchAgent`)
An intelligent web research agent that searches multiple sources, extracts information, and provides consensus-based answers with confidence scores.

**Features:**
- 🔍 Multi-source web search via SerpAPI
- 📄 Content extraction with BeautifulSoup
- 🧠 Consensus analysis using fuzzy matching
- 📊 Confidence scoring based on source agreement
- 📚 Structured output with citations
- 💻 CLI interface

**Tech Stack:** Python, SerpAPI, BeautifulSoup, Requests

[➡️ View Research Agent README](./ResearchAgent/README.md)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Google AI API Key (for E-Commerce Assistant)
- SerpAPI Key (for Research Agent)

### Choose Your Project

#### Option 1: E-Commerce Shopping Assistant

```bash
cd Ecommerce
python3 -m venv .venv
source .venv/bin/activate
pip install fasthtml python-fasthtml pydantic-ai python-dotenv logfire

# Create .env file with your Google API key
echo "GOOGLE_API_KEY=your_key_here" > .env

# Run the application
python main.py
# Visit http://localhost:5001
```

#### Option 2: Research Agent

```bash
cd ResearchAgent
python3 -m venv .venv
source .venv/bin/activate
pip install requests beautifulsoup4 python-dotenv

# Create .env file with your SerpAPI key
echo "SERPAPI_KEY=your_key_here" > .env

# Run the agent
python research_agent.py
```

---

## 📂 Repository Structure

```
pydantic-ai-assignment/
├── README.md                          # This file
├── Ecommerce/                         # E-Commerce Shopping Assistant
│   ├── main.py                        # FastHTML web application
│   ├── tools.py                       # PydanticAI agent and tools
│   ├── agent.py                       # CLI version
│   ├── .env                           # API keys (not committed)
│   ├── .gitignore                     # Git ignore rules
│   └── README.md                      # Detailed setup guide
│
└── ResearchAgent/                     # Web Research Agent
    ├── research_agent.py              # Main agent implementation
    ├── pyproject.toml                 # Project dependencies
    ├── .env                           # API keys (not committed)
    ├── .gitignore                     # Git ignore rules
    └── README.md                      # Detailed setup guide
```

---

## 🎯 Use Cases

### E-Commerce Shopping Assistant
Perfect for:
- Learning PydanticAI tool calling
- Building conversational commerce apps
- Understanding state management in AI agents
- Creating modern web UIs with FastHTML
- Implementing natural language interfaces

### Research Agent
Perfect for:
- Automated web research
- Information synthesis from multiple sources
- Fact-checking with confidence scores
- Building research assistants
- Learning web scraping and NLP

---

## 🔑 Getting API Keys

### Google AI API Key (E-Commerce)
1. Visit https://aistudio.google.com/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy and save in `Ecommerce/.env`

### SerpAPI Key (Research Agent)
1. Visit https://serpapi.com/
2. Sign up for free account (100 searches/month)
3. Copy API key from dashboard
4. Save in `ResearchAgent/.env`

---

## 🛡️ Security Best Practices

- ✅ Never commit `.env` files to git
- ✅ Both projects include `.gitignore` for protection
- ✅ Rotate API keys if accidentally exposed
- ✅ Monitor API usage to prevent abuse
- ✅ Don't share screenshots containing API keys

---

## 🎨 Screenshots

### E-Commerce Shopping Assistant
Beautiful 3-panel layout with:
- Product catalog (left)
- Chat interface (middle)
- Shopping cart (right)

### Research Agent
CLI interface showing:
- Top 3 findings with sources
- Majority consensus answer
- Confidence percentage

---

## 🔧 Troubleshooting

### Common Issues

**E-Commerce Assistant:**
- Port 5001 already in use → Kill existing process or change port
- API key error → Check `.env` file and key validity
- Module not found → Activate virtual environment and reinstall

**Research Agent:**
- SERPAPI_KEY not found → Check `.env` file exists
- Too many requests → Free tier limit reached (100/month)
- No results → Check internet connection

See individual project READMEs for detailed troubleshooting.

---

## 📚 Technologies Used

| Technology | E-Commerce | Research Agent |
|------------|-----------|----------------|
| PydanticAI | ✅ | ❌ |
| FastHTML | ✅ | ❌ |
| Google Gemini | ✅ | ❌ |
| SerpAPI | ❌ | ✅ |
| BeautifulSoup | ❌ | ✅ |
| Python | ✅ | ✅ |
| HTMX | ✅ | ❌ |

---

## 🎓 Learning Outcomes

After exploring these projects, you'll understand:

- **PydanticAI Fundamentals**: Agent creation, tool calling, system prompts
- **State Management**: Managing persistent data in AI agents
- **Web Development**: Building UIs with FastHTML and HTMX
- **Natural Language Processing**: Understanding user intent
- **Web Scraping**: Extracting data from websites
- **API Integration**: Working with Google AI and SerpAPI
- **Consensus Algorithms**: Comparing and synthesizing information
- **Security**: Protecting API keys and sensitive data

---

## 📖 Documentation Links

- [PydanticAI Documentation](https://ai.pydantic.dev/)
- [FastHTML Documentation](https://fastht.ml/)
- [Google AI Studio](https://aistudio.google.com/)
- [SerpAPI Documentation](https://serpapi.com/docs)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---

## 📝 License

Educational use only.

---

## 🤝 Contributing

This is an educational project. Feel free to fork and experiment!

---

## 💡 Future Enhancements

### E-Commerce Assistant
- [ ] Product search functionality
- [ ] Price calculation and checkout
- [ ] Order history tracking
- [ ] User authentication
- [ ] Payment integration

### Research Agent
- [ ] Multiple search engine support
- [ ] Fact-checking against trusted sources
- [ ] Citation formatting (APA, MLA)
- [ ] Export to JSON/CSV
- [ ] Web UI interface

---

**Built with ❤️ using PydanticAI and modern Python tools**










