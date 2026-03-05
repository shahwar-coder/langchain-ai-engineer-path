from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# Step 1: Define chat template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

# Step 2: Create chat history
chat_history = [
    HumanMessage(content="What is cricket?"),
    AIMessage(content="Cricket is a bat and ball sport.")
]

# Step 3: Format messages
formatted_prompt = chat_template.format_messages(
    chat_history=chat_history,
    question="Explain DRS simply."
)

# See what it creates
for msg in formatted_prompt:
    print(msg)

# [
#     SystemMessage(
#         content='You are a helpful assistant.',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     HumanMessage(
#         content='What is cricket?',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     AIMessage(
#         content='Cricket is a bat and ball sport.',
#         additional_kwargs={},
#         response_metadata={},
#         tool_calls=[],
#         invalid_tool_calls=[]
#     ),
#     HumanMessage(
#         content='Explain DRS simply.',
#         additional_kwargs={},
#         response_metadata={}
#     )
# ]