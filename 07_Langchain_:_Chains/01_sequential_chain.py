from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# ==========================
# Model
# ==========================

model = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)

# ==========================
# Output Parser
# ==========================

parser = StrOutputParser()

# ==========================
# Prompt 1: Report
# ==========================

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"]
)

# ==========================
# Prompt 2: Summary
# ==========================

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text:\n{text}",
    input_variables=["text"]
)

# ==========================
# Single Sequential Pipeline
# ==========================

chain = (
    prompt1
    | model
    | parser
    | prompt2
    | model
    | parser
)

# ==========================
# Execute
# ==========================

result = chain.invoke({
    "topic": "Unemployment in India"
})

print("\nSummary")
print("-" * 40)
print(result)


"""
SEQUENTIAL CHAIN (LANGCHAIN LCEL) — SIMPLE EXPLANATION
======================================================

Goal
----
Build a pipeline where the output of one AI step becomes the
input of the next AI step.

Here the pipeline does:

1️⃣ Generate a detailed report on a topic
2️⃣ Convert that report into a 5-point summary


------------------------------------------------------------
1️⃣ Model Initialization
------------------------------------------------------------

model = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)

• Uses a local Ollama LLM
• temperature=0 → deterministic output


------------------------------------------------------------
2️⃣ Output Parser
------------------------------------------------------------

parser = StrOutputParser()

Purpose:
Extract plain text from the model response.

Normally the model returns:

AIMessage(
    content="generated text"
)

StrOutputParser converts it into:

"generated text"

This makes it usable by the next step.


------------------------------------------------------------
3️⃣ Prompt 1 — Report Generator
------------------------------------------------------------

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}"
)

Example formatted prompt:

"Generate a detailed report on Unemployment in India"


------------------------------------------------------------
4️⃣ Prompt 2 — Summary Generator
------------------------------------------------------------

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text:\n{text}"
)

Example formatted prompt:

"Generate a 5 pointer summary from the following text:
<report text>"


------------------------------------------------------------
5️⃣ Sequential Chain
------------------------------------------------------------

chain = (
    prompt1
    | model
    | parser
    | prompt2
    | model
    | parser
)

This creates a **sequential AI pipeline**.

Each step passes its output to the next step.


------------------------------------------------------------
6️⃣ Execution Flow
------------------------------------------------------------

Input:

{"topic": "Unemployment in India"}

Step-by-step:

1️⃣ PromptTemplate (prompt1)
   Creates report prompt.

2️⃣ Model
   Generates detailed report.

3️⃣ StrOutputParser
   Extracts report text.

4️⃣ PromptTemplate (prompt2)
   Injects report into summary prompt.

5️⃣ Model
   Generates 5-point summary.

6️⃣ StrOutputParser
   Extracts final summary text.


------------------------------------------------------------
7️⃣ Visual Pipeline
------------------------------------------------------------

User Input
   ↓
PromptTemplate (Report)
   ↓
LLM
   ↓
Text Parser
   ↓
PromptTemplate (Summary)
   ↓
LLM
   ↓
Text Parser
   ↓
Final Output


------------------------------------------------------------
8️⃣ Why This Is Called Sequential Chain
------------------------------------------------------------

Because steps run **one after another**.

Output of Step 1 → becomes input of Step 2.


------------------------------------------------------------
9️⃣ Mental Model
------------------------------------------------------------

Think of it like a factory line:

Topic
  ↓
Machine 1 → Writes Report
  ↓
Machine 2 → Reads Report
  ↓
Machine 2 → Produces Summary


------------------------------------------------------------
Key Idea
------------------------------------------------------------

Sequential chains allow you to build **multi-step AI workflows**
where each model step processes the result of the previous one.
"""