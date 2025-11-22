# Ecommerce Agent Example

This repository contains a state-aware ecommerce assistant implemented as a single-file Python module using `pydantic_ai`, `logfire`, and `python-dotenv`. The agent manages a persistent shopping cart, supports multi-turn conversation, and exposes tools for cart and product management.

## Repository Structure

```
/your-repo/
├── ecommerce_agent_app.py         # Main agent implementation (single file)
├── README.md                      # This file
└── tests/
    └── test_cart.py               # Cart logic tests
```

## Setup

1. Install dependencies:

```sh
pip install pydantic-ai logfire python-dotenv pytest
```

2. (Optional) Set environment variables in a `.env` file (e.g., to override model name):

```
MODEL_NAME=gpt-3.5-turbo
```

## Running the CLI Demo

```sh
python ecommerce_agent_app.py
```

- Type your queries to interact with the agent.
- Type `demo` to see a 3-turn example conversation.
- Type `exit` to quit.

## Running Tests

```sh
pytest
```

## Example Conversation

```
Ecommerce Agent CLI. Type 'demo' to see an example conversation. Type 'exit' to quit.
You: demo
Demo conversation:

User: Add 2 of p1 to my cart.
Assistant: Added 2 of 'p1' to cart.

User: Remove 1 of p1.
Assistant: Removed 1 of 'p1' from cart.

User: Show me my cart.
Assistant: Cart: Widget (x1)
```

## Features
- Persistent, async-safe cart with atomic file storage
- Tools for add, update, remove, view, clear, and snapshot cart
- Product details and inventory checking tools (mocked)
- Multi-turn conversation with stateful message history
- CLI demo and test suite

## Notes
- Product catalog is in-memory and includes a few sample products (p1, p2, p3)
- Cart state is saved to `cart_state.json` in the working directory
- All agent responses are coerced to strings for CLI output
- For debugging or UI, use the `raw_cart` or `snapshot_state` tools

---

For more details, see the code in `ecommerce_agent_app.py` and the tests in `tests/test_cart.py`.










