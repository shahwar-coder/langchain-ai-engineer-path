"""
RunnableLambda takes an input, applies a custom Python function to it,
and returns the transformed output.

It is used to insert custom logic such as preprocessing, transformation,
filtering, or API calls inside a LangChain pipeline.

Example:

from langchain_core.runnables import RunnableLambda

def to_upper(text):
    return text.upper()

upper = RunnableLambda(to_upper)

result = upper.invoke("black hole")
print(result)

Output:
BLACK HOLE
"""