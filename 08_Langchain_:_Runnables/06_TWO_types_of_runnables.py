"""
Runnable Hierarchy in LangChain

LangChain Runnables can be broadly divided into two categories.

                Runnables
                   │
        ┌──────────┴──────────┐
        │                     │
Task-Specific Runnables   Runnable Primitives

--------------------------------------------------

1. Task-Specific Runnables

Definition:
These are core LangChain components that have been converted
into Runnables so they can be used inside pipelines.

Purpose:
They perform actual AI-related tasks such as prompting,
model inference, and document retrieval.

Examples:

ChatOpenAI / ChatOllama
→ Executes the LLM and generates responses.

PromptTemplate
→ Formats prompts dynamically using input variables.

Retriever
→ Fetches relevant documents from a vector database
   during retrieval tasks like RAG.

These components represent the functional steps
in an AI pipeline.

Example pipeline:

Input
  ↓
PromptTemplate
  ↓
LLM
  ↓
Output

--------------------------------------------------

2. Runnable Primitives

Definition:
These are fundamental building blocks used to structure
and control how runnables execute.

Purpose:
They orchestrate execution flow — determining how different
steps run (sequentially, in parallel, or conditionally).

Examples:

RunnableSequence
→ Runs steps sequentially (created using the | operator).

RunnableParallel
→ Executes multiple runnables simultaneously.

RunnableMap
→ Applies the same input across multiple runnables.

RunnableBranch
→ Implements conditional logic (if-else routing).

RunnableLambda
→ Wraps custom Python functions into runnable blocks.

RunnablePassthrough
→ Forwards input unchanged while optionally adding fields.

--------------------------------------------------

Key Idea

Task-Specific Runnables perform the work.

Runnable Primitives control how the work is organized
and executed inside a pipeline.

--------------------------------------------------

Mental Model

Task Components:
Prompt → LLM → Retriever

Execution Controllers:
Sequence / Parallel / Branch / Lambda

Together they form flexible AI pipelines.

--------------------------------------------------

Summary

Task-Specific Runnables = Components that perform AI tasks.

Runnable Primitives = Components that control execution flow.

Both work together to build modular and composable
LangChain pipelines.
"""