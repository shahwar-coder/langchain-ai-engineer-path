# It returns the exact same thing

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

passthrough = RunnablePassthrough()

# Example 1 : Same number returned
print("Example 1")
print(passthrough.invoke(34))


# Example 2 : Same string printed
print("\nExample 2")
print(passthrough.invoke("Artificial Intelligence"))


# Example 3 : Passthrough inside a parallel chain
# Keeps original input while another operation modifies it
parallel_chain = RunnableParallel({
    "original": RunnablePassthrough(),
    "square": lambda x: x * x
})

print("\nExample 3")
print(parallel_chain.invoke(6))


# Example 1
# 34

# Example 2
# Artificial Intelligence

# Example 3
# {'original': 6, 'square': 36}