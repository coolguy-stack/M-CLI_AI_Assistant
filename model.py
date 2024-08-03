import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('API_KEY')

conversation_history = []

def get_user_input():
    user_message = input("You: ")
    if user_message.lower() == 'exit':
        print("Goodbye!")
        return

    conversation_history.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        ai_response = response.choices[0].message["content"]
        print(f"M: {ai_response}")

        conversation_history.append({"role": "assistant", "content": ai_response})
    except Exception as e:
        print(f"Error: {e}")

    get_user_input()

print("Welcome! Let's chat. Type 'exit' to end the conversation.")
conversation_history.append({"role": "assistant", "content": "Hello! I am M, your personal CLI AI Assistant!."})

get_user_input()
