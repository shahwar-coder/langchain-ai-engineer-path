from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(model="llama3.2:1b")

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)

# Output:
# [
#     SystemMessage(
#         content='You are a helpful assistant',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     HumanMessage(
#         content='Tell me about Langchain',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     AIMessage(
#         content="LangChain is an open-source, self-service platform that enables developers to build and deploy chatbots for various platforms, including websites, mobile apps, and messaging services. It was founded in 2017 by Daniel Chavkin, who is also the CEO of Dialogflow.\n\nLangChain allows users to create chatbots without requiring extensive coding knowledge or technical expertise. The platform provides a set of APIs and tools that enable developers to build and deploy chatbots using various programming languages, including Python, JavaScript, and TypeScript.\n\nOne of the key features of LangChain is its ability to integrate with popular platforms like Google Drive, Dropbox, and Amazon S3, making it easy to store and manage chatbot data. The platform also supports multiple messaging channels, including SMS, WhatsApp, Facebook Messenger, and more.\n\nLangChain has gained popularity among developers due to its ease of use, flexibility, and scalability. The platform is designed to be scalable and can handle high volumes of conversations, making it suitable for large enterprises and businesses with complex chatbot requirements.\n\nSome key benefits of using LangChain include:\n\n* Easy integration with popular platforms\n* Scalable and flexible architecture\n* Highly customizable API\n* Supports multiple programming languages\n\nHowever, as with any technology, there are also potential drawbacks to consider. Some users have reported issues with the platform's documentation and support, while others have mentioned that it may not be suitable for very complex chatbot requirements.\n\nOverall, LangChain is a powerful tool that can help developers build high-quality chatbots without requiring extensive coding knowledge or technical expertise. Its ease of use, flexibility, and scalability make it an attractive option for businesses looking to implement chatbots in their applications.",
#         additional_kwargs={},
#         response_metadata={},
#         tool_calls=[],
#         invalid_tool_calls=[]
#     )
# ]