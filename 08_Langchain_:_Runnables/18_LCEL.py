"""
LCEL (LangChain Expression Language)

LCEL is a simple way to build LangChain pipelines by connecting
runnables using the pipe operator (|).

Instead of manually creating a RunnableSequence like:

RunnableSequence(r1, r2, r3)

LCEL allows us to write the same pipeline more clearly as:

r1 | r2 | r3

Here:
r1 → runs first
r2 → takes output of r1
r3 → takes output of r2

Example:

prompt | model | parser

Flow:
Input → PromptTemplate → LLM → OutputParser → Final Output

LCEL makes runnable pipelines easier to read, compose,
and maintain compared to manually defining RunnableSequence.
"""