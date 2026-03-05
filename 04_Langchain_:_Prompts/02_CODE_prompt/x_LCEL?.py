'''
Q1. What is LCEL in LangChain?

A.
LCEL stands for LangChain Expression Language.
It is a simple way to connect different components
like prompts, LLMs, and output parsers
using a clean, readable syntax.
'''
# Example:
# prompt | model | parser
# This builds a full pipeline in one line.



'''
Q2. What problem does LCEL solve?

A.
Before LCEL, building chains required more boilerplate code.
LCEL makes pipelines:
- Shorter
- Clearer
- Easier to compose
It simplifies multi-step LLM workflows.
'''
# Example:
# Instead of defining separate chain classes,
# You directly compose components using | operator.



'''
Q3. What is the core idea behind LCEL?

A.
Each component takes input and produces output.
LCEL allows you to connect them like pipes.
Output of one becomes input of the next.
'''
# Example:
# User input → PromptTemplate → LLM → OutputParser



'''
Q4. What does the "|" (pipe) operator mean in LCEL?

A.
It means "pass output to the next step".
Just like Unix pipes or functional composition.
'''
# Example:
# step1 | step2 | step3
# step1 output → step2 input → step3 input



'''
Q5. What is a simple LCEL example?

A.
Here is a minimal pipeline:
'''
# Example:
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
#
# prompt = ChatPromptTemplate.from_template("Explain {topic} simply")
# model = ChatOpenAI()
#
# chain = prompt | model
#
# chain.invoke({"topic": "transformers"})
#
# Flow:
# Input → Prompt → Model → Output



'''
Q6. Why is LCEL important for building RAG systems?

A.
Because RAG has multiple steps:
- Retrieve documents
- Format prompt
- Call LLM
LCEL lets you compose these steps cleanly.
'''
# Example:
# retriever | format_docs | prompt | model



'''
Q7. Strong mental model of LCEL:

A.
Think of LCEL as Lego blocks.
Each block does one job.
You snap them together to build a pipeline.
'''
# Example:
# Block 1: Prompt
# Block 2: LLM
# Block 3: Parser
# Connected using | operator



'''
Q8. Interview-ready definition of LCEL:

A.
LCEL (LangChain Expression Language) is a composable
pipeline syntax in LangChain that allows developers
to declaratively connect prompts, models, retrievers,
and parsers using functional composition,
reducing boilerplate and improving readability.
'''
# Example:
# prompt | model | parser
