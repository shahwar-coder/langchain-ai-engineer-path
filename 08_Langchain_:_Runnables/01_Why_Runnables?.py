'''
Why Runnables Were Introduced in LangChain

Earlier versions of LangChain used many different Chain classes
like LLMChain, SequentialChain, RouterChain, etc. This created
several problems.

Problems with Old Chains
- Too many chain classes to learn
- Hard to build multi-step pipelines
- Difficult to add custom logic or branching
- Inconsistent methods like run(), predict(), call(), invoke()

This made complex workflows messy and harder to maintain.

--------------------------------------------------

Solution: Runnables

LangChain introduced Runnables as a unified execution model.

Now every component behaves like a Runnable:
- PromptTemplate
- LLM
- OutputParser
- Custom Python functions
- Chains

All follow the same interface:

invoke()  → run once
batch()   → run multiple inputs
stream()  → stream outputs

--------------------------------------------------

Key Benefit

Runnables can be easily connected using the pipe operator:

    chain = prompt | model | parser

This creates a clean pipeline where the output of one
step automatically becomes the input of the next.

--------------------------------------------------

Common Runnable Types

RunnableSequence
Runs steps sequentially (created automatically using |).

RunnableLambda
Wraps custom Python functions inside a runnable.

RunnableBranch
Adds conditional logic (if/else routing).

RunnablePassthrough
Passes input forward while adding new fields.

--------------------------------------------------

Summary

Runnables simplify LangChain by providing a consistent
way to build AI pipelines where each component connects
cleanly in a modular workflow.
'''