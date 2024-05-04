import google.generativeai as genai

class GenAIException(Exception):
    pass

class ChatBot:
    CHATBOT_NAME = "Genie"

    def __init__(self, api_key):
        self.genai = genai
        self.genai.configure(api_key=api_key)
        self.model = self.genai.GenerativeModel("gemini-pro")
        self.conversation = None
        self._conversation_history = []

    def send_prompt(self, prompt, temperature=0.1):
        if temperature < 0 or temperature > 1:
            raise GenAIException("Temperature must be between 0 and 1")

        if not prompt:
            raise GenAIException("Prompt cannot be empty")

        try:
            response = self.conversation.send_message(
                content=prompt,
                generation_config=self._generation_config(temperature),
            )
            response.resolve()
            return f'{response.text}\n' + '----' * 20
        except Exception as e:
            raise GenAIException(str(e))

    def start_conversation(self):
         self.conversation = self.model.start_chat(history=self._conversation_history)

    def _generation_config(self, temperature):
         return self.genai.types.GenerationConfig(
            temperature=temperature
        )

