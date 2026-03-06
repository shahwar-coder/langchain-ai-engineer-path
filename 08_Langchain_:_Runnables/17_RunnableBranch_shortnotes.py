"""
RunnableBranch takes an input and routes it to different runnables
based on a condition, similar to an if/else statement.

It checks each condition and executes the runnable associated
with the first matching condition.

Example:

from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
    (lambda x: x > 10, lambda x: "Number is greater than 10"),
    (lambda x: x <= 10, lambda x: "Number is 10 or smaller"),
)

result = branch.invoke(7)
print(result)

Output:
Number is 10 or smaller
"""