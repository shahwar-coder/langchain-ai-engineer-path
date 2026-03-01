from langchain_core.prompts import ChatPromptTemplate
# No need of importing SystemMessage etc....

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({
    'domain':'cricket',
    'topic':'DRS'
})

print(prompt)

# messages = [
#     SystemMessage(
#         content='You are a helpful cricket expert',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     HumanMessage(
#         content='Explain in simple terms, what is DRS',
#         additional_kwargs={},
#         response_metadata={}
#     )
# ]