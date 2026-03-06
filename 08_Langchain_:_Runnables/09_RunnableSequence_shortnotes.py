"""
RunnableSequence executes multiple runnables step-by-step, where the output of one step
becomes the input to the next step.

It takes an initial input, processes it through each runnable in sequence,
and returns the final output produced by the last runnable.

Example:

from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template("Explain {topic} in simple terms")
model = ChatOllama(model="llama3.2:1b")
parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)

result = chain.invoke({"topic": "Black holes"})
print(result)

Flow:
Input → PromptTemplate → LLM → OutputParser → Final Output
"""