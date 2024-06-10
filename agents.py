#%%
import requests


def generate_text(prompt):
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOGZmNzcyMDQtZDI0ZS00YzQyLThhMDItODg3OTFlODcwNjBlIiwidHlwZSI6ImFwaV90b2tlbiJ9.VgtDSYHVcTvRMjA356ZeI7jSAKx4eUMis1dkFh0Ks68"
    
    url = "https://api.edenai.run/v2/text/generation"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "providers": "openai",
        "text": prompt,
        "temperature": 0.2,
        "max_tokens": 250,
        "fallback_providers": "cohere",
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error generating text: {error}")
        raise


#result = generate_text("Hi how are you?")
#print(result)

# %%
def get_ai_response(user_input):
    response = generate_text(user_input)
    
    
    try:
        generated_text = response['openai']['generated_text']  
        return generated_text
    except KeyError:
        return "I'm sorry, I couldn't generate a response."


# %%
def ai_interaction_loop():
    print("Welcome to the AI Agent! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        ai_response = get_ai_response(user_input)
        print(f"AI: {ai_response}")
# %%
if __name__ == "__main__":
    ai_interaction_loop()
