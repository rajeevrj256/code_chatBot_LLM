from langchain_openai import ChatOpenAI

class OpenAIChatbot:
    def __init__(self, api_key, model="gpt-3.5-turbo", temperature=0.7):
        self.chat_model = ChatOpenAI(
            openai_api_key=api_key,
            model=model,
            temperature=temperature
        )

    def generate_response(self, conversation_history):
        return self.chat_model(conversation_history).content
