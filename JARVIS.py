import requests

class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, trigger, target_state, action):
        self.transitions[trigger] = (target_state, action)

    def handle_input(self, trigger, context):
        if trigger in self.transitions:
            target_state, action = self.transitions[trigger]
            return action(context)
        else:
            return "I'm sorry, I don't understand that."

class Conversation:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def set_initial_state(self, state_name):
        if state_name in self.states:
            self.current_state = self.states[state_name]
        else:
            print(f"State '{state_name}' does not exist.")

    def trigger_transition(self, trigger, context):
        if self.current_state:
            return self.current_state.handle_input(trigger, context)
        else:
            return "No current state set."

class CodeGenerationAgent(Conversation):
    def __init__(self):
        super().__init__()
        self.headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmM3OWJhOGYtYjNiOC00OTkyLWJkNjItYTA1YzA1Zjk2Zjg2IiwidHlwZSI6ImFwaV90b2tlbiJ9.mvKiWHbwtfbtuhvzJ-sYp5xhnJGBE3H_L2ehQTyaCig"}
        self.url = "https://api.edenai.run/v2/text/code_generation"

        default_state = State("default")

        default_state.add_transition("generate", default_state, self.generate_code)

        self.add_state(default_state)
        self.set_initial_state("default")

    def generate_code(self, context):
        prompt = input("Enter the prompt: ")
        instruction = input("Enter the instruction: ")
        payload = {
            "providers": "openai",
            "prompt": prompt,
            "instruction": instruction,
            "temperature": 0.1,
            "max_tokens": 500,
        }

        try:
            response = requests.post(self.url, json=payload, headers=self.headers)
            response.raise_for_status()
            result = response.json()
            generated_code = result['openai']['generated_text']
            return generated_code
        except requests.exceptions.RequestException as error:
            print(f"Error generating code: {error}")
            return "I'm sorry, I couldn't generate code."

if __name__ == "__main__":
    agent = CodeGenerationAgent()
    print("Welcome to the Code Generation AI Agent! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        ai_response = agent.trigger_transition("generate", {})
        print(f"AI: {ai_response}")
