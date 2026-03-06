"""
Runnables in LangChain: Solving the Standardization Problem

Earlier versions of LangChain relied on many different chain classes such as:
- LLMChain
- SequentialChain
- SimpleSequentialChain
- RouterChain
- ConversationChain

Each chain type had its own behavior and execution methods like:
.run()
.predict()
.call()
.invoke()

This created several problems for developers.

--------------------------------------------------

Problems Before Runnables

1. Too Many Chain Classes
Developers had to learn many different chain types depending on the use case.
This made LangChain harder to learn and maintain.

2. Lack of Standardization
Different components used different execution methods, which created confusion
and inconsistent code patterns.

3. Hard to Compose Workflows
Building pipelines like:

    Prompt → LLM → Parser → Another Prompt → LLM

required nesting different chain objects. This made the code complex and harder
to read.

4. Poor Flexibility
It was difficult to:
- reuse components
- insert custom Python logic
- build branching workflows
- extend pipelines cleanly

As LangChain grew, these problems became more noticeable.

--------------------------------------------------

Solution: Runnables

LangChain introduced "Runnables" as a unified abstraction.

A Runnable is a standard execution block that receives input,
processes it, and returns output.

Now many components in LangChain behave as Runnables:

- PromptTemplate
- LLM / Chat models
- Output Parsers
- Custom Python functions
- Chains themselves

All of them follow the same interface.

--------------------------------------------------

Standard Runnable Methods

Every runnable supports the same methods:

invoke()   → run once with a single input
batch()    → run multiple inputs at once
stream()   → stream tokens or partial outputs

Example mental model:

    Input
      ↓
   Runnable
      ↓
   Runnable
      ↓
   Runnable
      ↓
    Output

Each block processes data and passes it to the next step.

--------------------------------------------------

Composable Pipelines using LCEL

Runnables can be connected using the pipe operator "|".

Example:

    chain = prompt | model | parser

This creates a clean pipeline:

    PromptTemplate → LLM → OutputParser

The output of one step automatically becomes the input
to the next step.

--------------------------------------------------

Pipeline Example

Input
  ↓
PromptTemplate (formats the input)
  ↓
LLM (generates response)
  ↓
Parser (converts output to usable format)
  ↓
Final Output

Every step is a Runnable and uses the same invoke() method.

--------------------------------------------------

Why Runnables Are Important

1. Standard Interface
All components now follow the same execution pattern.

2. Simpler Code
Pipelines are easier to read and compose.

3. Better Modularity
Components can be swapped without rewriting the whole pipeline.

4. Flexible Workflows
Runnables enable advanced patterns like:
- branching logic
- conditional routing
- custom transformations
- parallel execution

--------------------------------------------------

Big Picture

Before Runnables:
LangChain consisted of many specialized chain classes with
different interfaces and execution patterns.

After Runnables:
LangChain provides a unified pipeline model where every
component is a Runnable with the same interface.

--------------------------------------------------

Final Mental Model

Think of Runnables as standardized building blocks
for AI pipelines.

    Input
      ↓
    Runnable
      ↓
    Runnable
      ↓
    Runnable
      ↓
    Output

This design makes LangChain pipelines easier to build,
extend, and maintain.
"""