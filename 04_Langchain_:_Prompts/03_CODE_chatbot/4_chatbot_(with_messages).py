from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(model="llama3.2:1b")

chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.strip().lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI: ", result.content)

print(f"Entire chat history:\n{chat_history}")

# [
#     SystemMessage(
#         content='You are a helpful AI assistant.',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     HumanMessage(
#         content='Hello',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     AIMessage(
#         content="How can I assist you today? Is there something on your mind that you'd like to talk about, or are you just looking for some general information or help with a task? I'm here to listen and provide assistance.",
#         additional_kwargs={},
#         response_metadata={},
#         tool_calls=[],
#         invalid_tool_calls=[]
#     ),
#     HumanMessage(
#         content='How are you?',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     AIMessage(
#         content="I'm doing well, thanks for asking. It's nice to have a chance to chat with you and let you know how I'm feeling. As a computer program, I don't have emotions or feelings like humans do, but I'm always ready to help and provide information when you need it. How about you? How's your day going so far?",
#         additional_kwargs={},
#         response_metadata={},
#         tool_calls=[],
#         invalid_tool_calls=[]
#     ),
#     HumanMessage(
#         content='What is Langchain ?',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     AIMessage(
#         content='Langchain is an open-source, distributed knowledge graph platform that allows users to create, edit, and query complex relationships between entities, documents, and concepts. It\'s designed to help teams work together more efficiently by providing a scalable and flexible way to store, manage, and analyze large amounts of data.\n\nThe platform uses a unique approach called "distributed hashing" to distribute the data across multiple machines, which enables it to handle vast amounts of data and provide fast lookup times. This makes Langchain particularly well-suited for applications where data is distributed across multiple locations or teams.\n\nOne of the key features of Langchain is its ability to store metadata alongside the actual data, which allows users to easily query and retrieve related information. This can be especially useful in applications such as knowledge graphs, search engines, and collaborative editing tools.\n\nLangchain has gained popularity among researchers and developers due to its flexibility, scalability, and ease of use. It\'s also been used in various domains, including artificial intelligence, natural language processing, and data analytics.',
#         additional_kwargs={},
#         response_metadata={},
#         tool_calls=[],
#         invalid_tool_calls=[]
#     ),
#     HumanMessage(
#         content='exit',
#         additional_kwargs={},
#         response_metadata={}
#     )
# ]


"""
CHAT LOOP — CONCISE FLOW
========================

1️⃣ Setup
- Initialize ChatOllama model
- Start chat_history with a SystemMessage

2️⃣ Loop
- Take user input
- Append HumanMessage to chat_history
- If "exit" → break
- Invoke model with FULL chat_history
- Append AIMessage response
- Print AI reply

3️⃣ Key Concept
- LLM is stateless.
- Memory = you re-send entire chat_history every time.
- Messages are structured:
    SystemMessage → behavior
    HumanMessage  → user input
    AIMessage     → model output

Flow:
User → Append → Invoke(full history) → Append → Repeat
"""