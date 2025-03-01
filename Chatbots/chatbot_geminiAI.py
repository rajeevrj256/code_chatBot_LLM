from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

class GeminiAIChatbot:
    def __init__(self, api_key, model="gemini-2.0-flash", temperature=0.7):
        self.chat_model = ChatGoogleGenerativeAI(
            openai_api_key=api_key,
            model=model,
            temperature=temperature
        )

    def generate_response(self, conversation_history):
        """
        Generate a response from GeminiAI.

        Args:
            conversation_history (list): List of dictionaries with 'role' and 'content'.

        Returns:
            str: The assistant's response.
        """
        # Convert plain dictionaries to LangChain message objects
        formatted_messages = []
        for message in conversation_history:
            if message["role"] == "system":
                formatted_messages.append(SystemMessage(content=message["content"]))
            elif message["role"] == "user":
                formatted_messages.append(HumanMessage(content=message["content"]))
            elif message["role"] == "assistant":
                formatted_messages.append(AIMessage(content=message["content"]))
            else:
                raise ValueError(f"Invalid role: {message['role']}")

        # Generate response using the LangChain model
        response = self.chat_model(formatted_messages)
        return response.content

