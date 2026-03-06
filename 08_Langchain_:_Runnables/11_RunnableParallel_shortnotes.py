"""
RunnableParallel executes multiple runnables at the same time using the same input.

Each runnable processes the input independently, and the outputs are combined
into a dictionary where each key corresponds to the result of a runnable.

Example:

from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2:1b")
parser = StrOutputParser()

joke_chain = PromptTemplate.from_template("Tell me a joke about {topic}") | model | parser
fact_chain = PromptTemplate.from_template("Give me one interesting fact about {topic}") | model | parser

parallel_chain = RunnableParallel(
    joke=joke_chain,
    fact=fact_chain
)

result = parallel_chain.invoke({"topic": "black holes"})
print(result)

Flow:
Input → (Joke Chain || Fact Chain run simultaneously) → Dictionary Output
"""