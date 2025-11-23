from pydantic_ai import Agent
import logfire
from dotenv import load_dotenv
import os
import time

# Load .env for API key
load_dotenv(override=True)

# Configure logfire for cleaner logs (optional)
logfire.configure()
logfire.instrument_pydantic_ai()


os.environ["GOOGLE_API_KEY"] = "AIzaSyBhnmNFSlcu2HLoP2ltKf7cDrofA97dhJw"

# Choose model
model = "google-gla:gemini-2.5-flash"
agent = Agent(model)

time.sleep(1)

# Keep track of message history for context
message_history = []

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye")
        break

    try:
        response = agent.run_sync(user_input, message_history=message_history)
        print("Agent:", response.output)

        # Keep conversation context
        message_history = response.all_messages()
    except Exception as e:
        print("Error:", e)
        print("Agent: Sorry, something went wrong.")
