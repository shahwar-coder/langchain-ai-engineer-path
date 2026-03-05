from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(model="llama3.2:1b")

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.strip().lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(f"Entire chat history:\n{chat_history}")

# Output:
# Entire chat history:
# [
#     'hi',
#     'Hello! How can I assist you today?',
#     'which one is greater 2 or 0',
#     '2 is greater than 0.',
#     'now multiply the bigger number with 10',
#     '2 multiplied by 10 is equal to 20.',
#     'exit'
# ]

'''
The problem here is, we don't know,
which is said by which?
You or AI?
'''

