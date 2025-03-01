from dotenv import load_dotenv
import os
from Chatbots.chatbot_core import ChatbotManager

# Load environment variables
load_dotenv()

# User selects LLM
llm_choice = input("Choose an LLM (openai, geminiai, huggingface): ").strip().lower()

# API keys for different LLMs
api_keys = {
    "openai": os.getenv("OPENAI_API_KEY"),
    "geminiai": os.getenv("GEMINIAI_API_KEY"),
}

# Initialize chatbot manager
chatbot_manager = ChatbotManager(llm_choice=llm_choice, api_keys=api_keys)

# Conversation history
conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("Exiting chat. Goodbye!")
        break

    # Add user input to the history
    conversation_history.append({"role": "user", "content": user_input})

    # Generate and display response
    response = chatbot_manager.generate_response(conversation_history)
    print(f"Bot: {response}")

    # Add bot response to the history
    conversation_history.append({"role": "assistant", "content": response})
