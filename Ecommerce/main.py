# app.py
from fasthtml.common import *
import asyncio
from tools import ecommerce_agent_instance, cart_items, get_message_history, AVAILABLE_PRODUCTS

app, rt = fast_app(pico=False)

StyleBlock = Style("""
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
background: #EEAECA;
background: radial-gradient(circle,rgba(238, 174, 202, 1) 0%, rgba(148, 187, 233, 1) 100%);
    min-height: 90vh;
}

.main-container {
    display: flex;
    gap: 15px;
    align-items: flex-start;
    height: 85vh;
}

.chat-container {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    height: 90%;
    display: flex;
    flex-direction: column;
    flex: 2;
    overflow: hidden;
}

.message {
    margin: 10px 0;
    padding: 12px 16px;
    border-radius: 18px;
    max-width: 70%;
    word-wrap: break-word;
    display: inline-block;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.user-message {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    float: right;
}

.bot-message {
    background: linear-gradient(135deg, #ffffff 0%, #ffeaa7 100%);
    color: #2d3436;
    float: left;
    border: 1px solid #fdcb6e;
}

.messages-container {
    flex: 1;
    overflow-y: auto;
    margin-bottom: 20px;
    padding: 10px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 8px;
}

.input-form {
    padding-top: 10px;
    border-top: 2px solid rgba(255, 255, 255, 0.5);
    display: flex;
    gap: 10px;
}

input[type='text'] {
    padding: 12px;
    border: 2px solid rgba(255, 255, 255, 0.6);
    border-radius: 25px;
    font-size: 16px;
    flex: 1;
    background: rgba(255, 255, 255, 0.8);
    transition: all 0.3s;
}

input[type='text']:focus {
    outline: none;
    border-color: #667eea;
    background: white;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

button {
    padding: 12px 18px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 20px;
    cursor: pointer;
    font-weight: 600;
    transition: transform 0.2s;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.cart-display {
    padding: 15px;
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    border: 2px solid rgba(255, 255, 255, 0.5);
    flex: 1;
    min-width: 280px;
    max-width: 350px;
    height: 90%;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
}

.cart-item-display {
    padding: 12px;
    margin: 6px 0;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.7);
    display: flex;
    justify-content: space-between;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);
}

.cart-empty {
    color: #636e72;
    font-style: italic;
    text-align: center;
    padding: 20px;
}

.products-container {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    flex: 1;
    min-width: 300px;
    max-width: 350px;
    height: 90%;
    overflow-y: auto;
}

.products-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 12px;
    margin-top: 15px;
}

.product-card {
    border: 2px solid rgba(255, 255, 255, 0.6);
    border-radius: 12px;
    padding: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s;
    background: rgba(255, 255, 255, 0.7);
}

.product-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    transform: translateY(-2px);
    background: rgba(255, 255, 255, 0.9);
}

.product-info {
    display: flex;
    align-items: center;
    gap: 10px;
}

.product-emoji {
    font-size: 32px;
}

.product-details {
    display: flex;
    flex-direction: column;
}

.product-name {
    font-weight: 600;
    color: #2d3436;
}

.product-price {
    color: #6c5ce7;
    font-size: 14px;
    font-weight: 600;
}

.add-btn {
    padding: 8px 16px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.3s;
    box-shadow: 0 2px 6px rgba(102, 126, 234, 0.3);
}

.add-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.5);
}

h3 {
    color: #2d3436;
    margin-top: 0;
    margin-bottom: 10px;
    font-size: 20px;
    text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5);
}
""")

@rt("/")
def index():
    return Titled("E-Commerce Assistant",
        Div(
            ProductsView(),
            Div(
                MessagesView(),
                Form(
                    Input(type="text", name="message", placeholder="Type your message and press Enter...", id="message-input", autofocus=True, autocomplete="off"),
                    Button("Send", type="submit"),
                    hx_post="/send",
                    hx_target="#messages",
                    hx_swap="beforeend",
                    cls="input-form"
                ),
                cls="chat-container"
            ),
            CartView(),
            cls="main-container"
        ),
        StyleBlock,
        Script("""
document.addEventListener('submit', function(e){
  // simple focus/scroll handling moved to server responses
}, true);
""")
    )

def ProductsView():
    products_list = []
    for product in AVAILABLE_PRODUCTS:
        products_list.append(
            Div(
                Div(
                    Div(product["emoji"], cls="product-emoji"),
                    Div(
                        Div(product["name"], cls="product-name"),
                        Div(f"${product['price']}", cls="product-price"),
                        cls="product-details"
                    ),
                    cls="product-info"
                ),
                Button("Add",
                    cls="add-btn",
                    hx_post=f"/add-product/{product['name']}",
                    hx_target="#cart-container",
                    hx_swap="outerHTML"
                ),
                cls="product-card"
            )
        )
    return Div(
        H3("Available Products"),
        Div(*products_list, cls="products-grid"),
        cls="products-container"
    )

def CartView():
    if not cart_items:
        return Div(H3("Shopping Cart"), Div("Your cart is empty", cls="cart-empty"), cls="cart-display", id="cart-container")
    children = [H3("Shopping Cart")]
    for product, qty in cart_items.items():
        children.append(Div(Span(product), Span(f"Qty: {qty}"), cls="cart-item-display"))
    return Div(*children, cls="cart-display", id="cart-container")

def MessagesView():
    messages = []
    for msg in get_message_history():
        if msg.get("kind") == "request":
            messages.append(Div(Div(msg["text"], cls="message user-message"), cls="message-wrapper"))
        elif msg.get("kind") == "response":
            messages.append(Div(Div(msg["text"], cls="message bot-message"), cls="message-wrapper"))
    return Div(*messages, cls="messages-container", id="messages")

@rt("/send")
async def send(message: str):
    if not message.strip():
        return ""
    # Get bot response
    bot_response = await ecommerce_agent_instance.run(message)
    # Return both user message and bot message
    return (
        Div(Div(message, cls="message user-message"), cls="message-wrapper"),
        Div(Div(bot_response, cls="message bot-message"), cls="message-wrapper",
            hx_get="/cart", hx_target="#cart-container", hx_swap="outerHTML", hx_trigger="load"),
        Script("""
            const input = document.getElementById('message-input');
            if (input) { input.value=''; input.focus(); }
            const messages = document.getElementById('messages');
            if (messages) { messages.scrollTop = messages.scrollHeight; }
        """)
    )

@rt("/cart")
def get_cart():
    return CartView()

@rt("/add-product/{product}")
async def add_product(product: str):
    # Add product to cart
    cart_items[product] = cart_items.get(product, 0) + 1
    # Return updated cart view
    return CartView()

if __name__ == "__main__":
    serve()
