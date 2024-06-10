import requests

class AIAgent:
    def __init__(self):
        self.api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOGZmNzcyMDQtZDI0ZS00YzQyLThhMDItODg3OTFlODcwNjBlIiwidHlwZSI6ImFwaV90b2tlbiJ9.VgtDSYHVcTvRMjA356ZeI7jSAKx4eUMis1dkFh0Ks68"
        self.url = "https://api.edenai.run/v2/text/generation"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.state = "default"
        self.memory = []  

    def generate_text(self, prompt):
        context = "\n".join(self.memory)  
        data = {
            "providers": "openai",
            "text": f"{context}\n{prompt}",  
            "temperature": 0.2,
            "max_tokens": 250,
            "fallback_providers": "cohere",
        }

        try:
            response = requests.post(self.url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(f"Error generating text: {error}")
            raise

    def get_memory_response(self, user_input):
        if "first thing i asked" in user_input.lower():
            if self.memory:
                for line in self.memory:
                    if line.startswith("You:"):
                        return line
            return "I don't remember anything from our conversation."

        return None

    def get_ai_response(self, user_input):
        memory_response = self.get_memory_response(user_input)
        if memory_response:
            return memory_response

        if self.state == "default":
            response = self.generate_text(user_input)
            try:
                generated_text = response['openai']['generated_text']
                self.memory.append(f"You: {user_input}")  
                self.memory.append(f"AI: {generated_text}")  
                return generated_text
            except KeyError:
                return "I'm sorry, I couldn't generate a response."

    
        elif self.state == "greeting":
            return "Hello! How can I assist you today?"

        if "help" in user_input.lower():
            self.state = "help"
            return "You asked for help. How can I assist you further?"

        elif "reset" in user_input.lower():
            self.state = "default"
            self.memory = [] 
            return "State has been reset."

    def ai_interaction_loop(self):
        print("Welcome to the AI Agent! Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            ai_response = self.get_ai_response(user_input)
            print(f"AI: {ai_response}")

if __name__ == "__main__":
    agent = AIAgent()
    agent.ai_interaction_loop()
