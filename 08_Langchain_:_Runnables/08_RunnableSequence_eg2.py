from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

# model
model = ChatOllama(model='llama3.2:1b')

# parser
parser = StrOutputParser()

# prompts
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

# chain
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

# visualize chain
print("\nChain Graph")
print("-" * 40)
chain.get_graph().print_ascii()

# execute
result = chain.invoke({'topic': 'Artificial Intelligence'})

# display
print(result)

# Output
# This joke is a play on words, exploiting the double meaning of "process" in two different contexts.
# In one sense, processing refers to the act of interpreting or understanding information, which is exactly what an artificial intelligence (AI) program does when it's learning and improving its algorithms.
# However, the second part of the sentence uses the word "process" also to refer to the emotional state of a person. In this case, the AI is going to therapy because it's feeling overwhelmed or struggling to cope with its emotions, rather than processing them as information.
# The joke relies on this clever double meaning to create a pun, which is a form of wordplay that uses words or phrases in a way that creates humor or surprise.


# =====


"""
RUNNABLE SEQUENCE (LANGCHAIN LCEL)
==================================

Goal
----
Create a simple multi-step AI pipeline:

1️⃣ Generate a joke
2️⃣ Explain the joke

Each step feeds its output into the next step.


------------------------------------------------------------
1️⃣ Model
------------------------------------------------------------

model = ChatOllama(model="llama3.2:1b")

• Local LLM running via Ollama
• Used for both joke generation and explanation


------------------------------------------------------------
2️⃣ Output Parser
------------------------------------------------------------

parser = StrOutputParser()

Why needed?

LLM returns an AIMessage object.

Example:
AIMessage(content="Here is the joke...")

But the next prompt expects **plain text**.

Parser converts:

AIMessage → string


------------------------------------------------------------
3️⃣ Prompt 1 — Joke Generator
------------------------------------------------------------

prompt1 = PromptTemplate(
    template="Write a joke about {topic}"
)

Input:
{ "topic": "Artificial Intelligence" }

Output example:
"Why did the AI go to therapy? Because it had too many processes to process!"


------------------------------------------------------------
4️⃣ Prompt 2 — Joke Explanation
------------------------------------------------------------

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}"
)

This prompt receives the **joke text** generated in Step 1.

Example input:
"Why did the AI go to therapy?..."


------------------------------------------------------------
5️⃣ RunnableSequence
------------------------------------------------------------

chain = RunnableSequence(
    prompt1,
    model,
    parser,
    prompt2,
    model,
    parser
)

RunnableSequence executes steps **one after another**.


------------------------------------------------------------
6️⃣ Execution Flow
------------------------------------------------------------

result = chain.invoke({"topic": "Artificial Intelligence"})


Step-by-step pipeline:

User Input
    │
    ▼
Prompt 1 (Generate Joke)
    │
    ▼
Model
    │
    ▼
Parser → converts to text
    │
    ▼
Prompt 2 (Explain Joke)
    │
    ▼
Model
    │
    ▼
Parser
    │
    ▼
Final Explanation


------------------------------------------------------------
7️⃣ Visual Pipeline
------------------------------------------------------------

Input (topic)
      │
      ▼
PromptTemplate
      │
      ▼
ChatOllama
      │
      ▼
StrOutputParser
      │
      ▼
PromptTemplate
      │
      ▼
ChatOllama
      │
      ▼
StrOutputParser
      │
      ▼
Final Output


------------------------------------------------------------
8️⃣ Key Idea
------------------------------------------------------------

RunnableSequence creates a **step-by-step AI workflow**
where each step feeds its result into the next step.

It is equivalent to writing:

step1_output = model(prompt1)
step2_output = model(prompt2(step1_output))


------------------------------------------------------------
9️⃣ LCEL Equivalent (Pipe Syntax)
------------------------------------------------------------

The same chain could also be written as:

chain = prompt1 | model | parser | prompt2 | model | parser


------------------------------------------------------------
10️⃣ When RunnableSequence Is Useful
------------------------------------------------------------

Use it when you want **multi-stage AI reasoning**:

• Generate → summarize
• Generate → explain
• Research → summarize
• Extract → transform
• Plan → execute

It is the simplest way to build **multi-step AI pipelines**.
"""