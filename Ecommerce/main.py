# app.py
from fasthtml.common import *
import asyncio
from tools import ecommerce_agent_instance, cart_items, get_message_history

app, rt = fast_app(pico=False)

StyleBlock = Style("""
body { font-family: Arial, sans-serif; max-width:1400px; margin:0 auto; padding:20px; background:#f5f5f5;}
.main-container { display:flex; gap:20px; align-items:flex-start; height:85vh; }
.chat-container{ background:white; padding:20px; border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.1); height:90%; display:flex; flex-direction:column; flex:2; overflow:hidden;}
.message{ margin:10px 0; padding:12px 16px; border-radius:18px; max-width:70%; word-wrap:break-word; display:inline-block;}
.user-message{ background:#0e6db8; color:white; float:right;}
.bot-message{ background:#e9ecef; color:#333; float:left;}
.messages-container{ flex:1; overflow-y:auto; margin-bottom:20px; padding:10px;}
.input-form{ padding-top:10px; border-top:2px solid #eee; display:flex; gap:10px;}
input[type='text']{ padding:12px; border:2px solid #ddd; border-radius:25px; font-size:16px; flex:1;}
button{ padding:12px 18px; background:#0e6db8; color:white; border:none; border-radius:20px; cursor:pointer;}
.cart-display{ padding:15px; background:white; border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.1); border:1px solid #dee2e6; flex:1; min-width:280px; max-width:350px; height:90%; display:flex; flex-direction:column; overflow-y:auto;}
.cart-item-display{ padding:8px 0; border-bottom:1px solid #dee2e6; display:flex; justify-content:space-between;}
.cart-empty{ color:#6c757d; font-style:italic;}
""")

@rt("/")
def index():
    return Titled("E-Commerce Assistant",
        Div(
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

if __name__ == "__main__":
    serve()
