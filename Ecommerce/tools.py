# ecommerce_tools.py
import asyncio
from typing import List, Dict
from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(override=True)

# Set up Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBhnmNFSlcu2HLoP2ltKf7cDrofA97dhJw"

cart_items: Dict[str, int] = {}
_message_history: List[dict] = []

# Product catalog
AVAILABLE_PRODUCTS = [
    {"name": "Apple", "price": 1.99, "emoji": "🍎"},
    {"name": "Banana", "price": 0.99, "emoji": "🍌"},
    {"name": "Orange", "price": 1.49, "emoji": "🍊"},
    {"name": "Grapes", "price": 3.99, "emoji": "🍇"},
    {"name": "Strawberry", "price": 4.99, "emoji": "🍓"},
    {"name": "Watermelon", "price": 5.99, "emoji": "🍉"},
    {"name": "Pineapple", "price": 3.49, "emoji": "🍍"},
    {"name": "Mango", "price": 2.99, "emoji": "🥭"},
    {"name": "Peach", "price": 2.49, "emoji": "🍑"},
    {"name": "Cherries", "price": 5.49, "emoji": "🍒"},
    {"name": "Kiwi", "price": 1.79, "emoji": "🥝"},
    {"name": "Avocado", "price": 2.29, "emoji": "🥑"},
]

# Create PydanticAI agent with Google Gemini
model = "google-gla:gemini-2.5-flash"
agent = Agent(
    model,
    system_prompt="""You are a helpful e-commerce shopping assistant.
You can help users manage their shopping cart by adding items, removing items, showing the cart, and clearing it.
When users ask to add items, extract the product names and quantities from their request.
Be friendly and conversational. Understand natural language requests like "I want to add apples and grapes" or "add 2 bananas".
Always use the available tools to modify the cart.

Available products: Apple, Banana, Orange, Grapes, Strawberry, Watermelon, Pineapple, Mango, Peach, Cherries, Kiwi, Avocado."""
)

@agent.tool
def add_to_cart(ctx: RunContext, product: str, quantity: int = 1) -> str:
    """Add a product to the shopping cart with specified quantity."""
    product = product.strip()
    cart_items[product] = cart_items.get(product, 0) + quantity
    return f"Added {quantity} × {product} to the cart."

@agent.tool
def remove_from_cart(ctx: RunContext, product: str) -> str:
    """Remove a product from the shopping cart."""
    product = product.strip()
    if product in cart_items:
        del cart_items[product]
        return f"Removed {product} from the cart."
    else:
        return f"{product} not found in cart."

@agent.tool
def show_cart(ctx: RunContext) -> str:
    """Show all items currently in the shopping cart."""
    if not cart_items:
        return "Your cart is empty."
    else:
        lines = [f"{p} — Qty: {q}" for p, q in cart_items.items()]
        return "Cart contains:\n" + "\n".join(lines)

@agent.tool
def clear_cart(ctx: RunContext) -> str:
    """Clear all items from the shopping cart."""
    cart_items.clear()
    return "Cart cleared."

class EcommerceAgent:
    """Wrapper for PydanticAI agent to work with the web app."""
    async def run(self, user_text: str) -> str:
        user_text = user_text.strip()
        _message_history.append({"kind": "request", "text": user_text})

        try:
            # Run the agent with the user's message
            result = await agent.run(user_text)
            resp = result.output
        except Exception as e:
            resp = f"Sorry, I encountered an error: {str(e)}"

        _message_history.append({"kind": "response", "text": resp})
        return resp

# single instance used by app.py
ecommerce_agent_instance = EcommerceAgent()

def get_message_history():
    return list(_message_history)
