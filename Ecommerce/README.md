# E-Commerce Shopping Assistant

An AI-powered e-commerce shopping assistant built with PydanticAI, FastHTML, and Google Gemini. Features a beautiful gradient UI with natural language cart management.

## Features

- **Natural Language Processing**: Chat with the AI to manage your shopping cart
- **Product Catalog**: Browse 12 available products with prices and emojis
- **Smart Cart Management**: Add, remove, view, and clear items with natural commands
- **Quick Add Buttons**: One-click product additions from the catalog
- **Beautiful Gradient UI**: Modern design with smooth animations and color gradients
- **Real-time Updates**: Cart updates instantly as you interact

## Prerequisites

- Python 3.10 or higher
- Google AI API Key (get one at https://aistudio.google.com/apikey)

## Installation

### 1. Clone the Repository

```bash
cd /Users/niharika/Documents/GitClones/pydantic-ai-assignment/Ecommerce
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fasthtml python-fasthtml pydantic-ai python-dotenv logfire
```

### 4. Configure API Key

Create or update the `.env` file in the project root:

```bash
# .env file
GOOGLE_API_KEY=your_api_key_here
```

**Get your API key:**
1. Visit https://aistudio.google.com/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and paste it in `.env`

## Running the Application

### Start the Server

```bash
source .venv/bin/activate
python main.py
```

The application will start at: **http://localhost:5001**

### Stop the Server

Press `Ctrl+C` in the terminal

## Usage

### Natural Language Commands

Type these commands in the chat:

- **Add items**: "I want to add 3 apples and 2 bananas"
- **Remove items**: "Remove one watermelon"
- **Remove all**: "Remove all grapes"
- **Show cart**: "Show my cart" or "What's in my cart?"
- **Clear cart**: "Empty cart" or "Clear my cart"

### Quick Add Buttons

Click the "Add" button next to any product in the catalog to instantly add 1 item to your cart.


## Project Structure

```
Ecommerce/
├── main.py              # FastHTML web application
├── tools.py             # PydanticAI agent and cart tools
├── agent.py             # CLI version (optional)
├── .env                 # API keys (DO NOT COMMIT)
├── .gitignore           # Git ignore rules
├── .venv/               # Virtual environment
└── README.md            # This file
```

## Security

- **Never commit `.env` files** to version control
- The `.gitignore` file prevents `.env` from being tracked
- If your API key is leaked, revoke it immediately and create a new one
- Never share screenshots containing API keys

## Troubleshooting

### "Address already in use" Error
```bash
# Kill the existing process
lsof -ti:5001 | xargs kill -9
# Then restart the server
python main.py
```

### "Module not found" Error
```bash
# Make sure virtual environment is activated
source .venv/bin/activate
# Reinstall dependencies
pip install fasthtml python-fasthtml pydantic-ai python-dotenv
```

### API Key Error (403 Forbidden)
- Your API key may be invalid or leaked
- Get a new key from https://aistudio.google.com/apikey
- Update the `.env` file with the new key
- Restart the server

### Messages Not Appearing
- Refresh the page (Cmd+R / F5)
- Clear browser cache if issues persist

## Technologies Used

- **PydanticAI**: AI agent framework with tool calling
- **FastHTML**: Modern Python web framework
- **Google Gemini 2.5 Flash**: Language model
- **HTMX**: Dynamic frontend updates
- **Python 3.14**: Programming language

## Features in Detail

### AI Agent Capabilities
- Understands natural language requests
- Extracts product names and quantities
- Handles plurals and variations ("apple" vs "apples")
- Provides conversational responses

### Cart Management
- Add multiple items in one command
- Remove specific quantities
- Keep track of item counts
- Persist during session

### UI/UX
- Gradient backgrounds (pink to blue)
- Hover animations on products and buttons
- Auto-scrolling chat
- Responsive layout
- Clean, modern design

## Development

### Modifying Products
Edit the `AVAILABLE_PRODUCTS` list in `tools.py`:

```python
AVAILABLE_PRODUCTS = [
    {"name": "ProductName", "price": 9.99, "emoji": "🍊"},
    # Add more products here
]
```

### Changing AI Model
Edit the model in `tools.py`:

```python
model = "google-gla:gemini-2.5-flash"  # or another model
```

### Customizing Styles
Modify the `StyleBlock` in `main.py` to change colors, fonts, or layout.

## License

This project is for educational purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify your API key is valid
3. Ensure all dependencies are installed
4. Check that port 5001 is available

---

