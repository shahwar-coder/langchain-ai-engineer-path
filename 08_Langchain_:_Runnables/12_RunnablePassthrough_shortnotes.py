"""
RunnablePassthrough takes an input and forwards it unchanged as the output.

It is used when you want to keep the original input while adding or computing
additional values in a pipeline.

Example:

from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough.assign(
    length=lambda x: len(x["text"])
)

result = chain.invoke({"text": "black hole"})
print(result)

Output:
{'text': 'black hole', 'length': 10}
"""