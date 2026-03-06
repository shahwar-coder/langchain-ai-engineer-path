from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

# model
model = ChatOllama(model='llama3.2:1b')

# parser
parser = StrOutputParser()

# prompt
prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# chain
chain = RunnableSequence(prompt, model, parser)

# execute
result = chain.invoke({'topic': 'Artificial Intelligence'})

# display
print(result)

# Output
# Why did the artificial intelligence system go on a diet?