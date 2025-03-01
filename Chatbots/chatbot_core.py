from Chatbots.chatbot_openAI import OpenAIChatbot
from Chatbots.chatbot_geminiAI import GeminiAIChatbot
#from Chatbots.chatbot_huggingFace import HuggingFaceChatbot

class ChatbotManager:
    def __init__(self, llm_choice, api_keys={}):
        
        self.llm_choice = llm_choice
        self.api_keys = api_keys
        self.chatbot = self._initialize_chatbot()

    def _initialize_chatbot(self):
        if self.llm_choice == "openai":
            return OpenAIChatbot(api_key=self.api_keys.get("openai"))
        elif self.llm_choice == "geminiai":
            return GeminiAIChatbot(api_key=self.api_keys.get("geminiai"))
        elif self.llm_choice == "huggingface":
            return HuggingFaceChatbot()
        else:
            raise ValueError(f"Unknown LLM choice: {self.llm_choice}")

    def generate_response(self, conversation_history):
        return self.chatbot.generate_response(conversation_history)
