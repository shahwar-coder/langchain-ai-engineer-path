# It returns the exact same thing

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

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

# joke creation chain
joke_gen_chain = RunnableSequence(prompt1, model, parser)

# joke expanation generation chain (but original joke made to carry forward here as it is, using RunnablePassthrough())
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

# final chain
chain = RunnableSequence(joke_gen_chain, parallel_chain)

# viz
print("Chain Graph")
print('-'*40)
chain.get_graph().print_ascii()

# execute
print("Result")
print('-'*40)
print(chain.invoke({'topic': 'Cricket'}))


# Chain Graph
# ----------------------------------------
#                   +-------------+                  
#                   | PromptInput |                  
#                   +-------------+                  
#                           *                        
#                           *                        
#                           *                        
#                 +----------------+                 
#                 | PromptTemplate |                 
#                 +----------------+                 
#                           *                        
#                           *                        
#                           *                        
#                   +------------+                   
#                   | ChatOllama |                   
#                   +------------+                   
#                           *                        
#                           *                        
#                           *                        
#                 +-----------------+                
#                 | StrOutputParser |                
#                 +-----------------+                
#                           *                        
#                           *                        
#                           *                        
#         +---------------------------------+        
#         | Parallel<joke,explanation>Input |        
#         +---------------------------------+        
#                  **              ***               
#               ***                   **             
#             **                        ***          
# +----------------+                       **        
# | PromptTemplate |                        *        
# +----------------+                        *        
#           *                               *        
#           *                               *        
#           *                               *        
#   +------------+                          *        
#   | ChatOllama |                          *        
#   +------------+                          *        
#           *                               *        
#           *                               *        
#           *                               *        
# +-----------------+               +-------------+  
# | StrOutputParser |               | Passthrough |  
# +-----------------+               +-------------+  
#                  **              **                
#                    ***        ***                  
#                       **    **                     
#         +----------------------------------+       
#         | Parallel<joke,explanation>Output |       
#         +----------------------------------+       
# Result
# ----------------------------------------
# {
#     "joke": "Why did the cricket go to the doctor?\n\nBecause it had a bad pitch.",

#     "explanation": """
# This joke is a play on words, using a pun to create humor.

# The word "pitch" has two meanings:

# 1. A type of ball used in sports like baseball and cricket.
# 2. A medical term for a condition that causes a person to feel unwell or experience symptoms.

# In this joke, the phrase "bad pitch" is a pun on both meanings.

# The listener expects it to be a literal reference to the cricket's performance on the field,
# but instead, it's a clever wordplay on the medical term.

# The joke is funny because it takes a common phrase and gives it an unexpected twist,
# creating a lighthearted and amusing connection between sports and medicine.
# """
# }


# ======


"""
RUNNABLEPASSTHROUGH + PARALLEL CHAIN
====================================

Goal
----
Generate a joke and ALSO explain the same joke,
while preserving the original joke in the final output.

Final output structure:

{
  "joke": "...",
  "explanation": "..."
}

Key Idea:
RunnablePassthrough lets us **forward existing data unchanged**
through the chain.


------------------------------------------------------------
1️⃣ Model
------------------------------------------------------------

model = ChatOllama("llama3.2:1b")

Used for:
• joke generation
• joke explanation


------------------------------------------------------------
2️⃣ Parser
------------------------------------------------------------

parser = StrOutputParser()

Converts:

AIMessage → plain string

Needed so the next prompt can consume the text.


------------------------------------------------------------
3️⃣ Prompt 1 — Joke Generator
------------------------------------------------------------

prompt1 = "Write a joke about {topic}"

Example input:

{"topic": "Cricket"}

Output example:

"Why did the cricket go to the doctor? Because it had a bad pitch."


------------------------------------------------------------
4️⃣ Prompt 2 — Joke Explanation
------------------------------------------------------------

prompt2 = "Explain the following joke - {text}"

This receives the joke text and explains it.


------------------------------------------------------------
5️⃣ Joke Generation Chain
------------------------------------------------------------

joke_gen_chain =
    prompt1 → model → parser

Output:

"Why did the cricket go to the doctor..."


------------------------------------------------------------
6️⃣ The Problem
------------------------------------------------------------

After generating the joke we want TWO things:

1️⃣ Keep the joke itself
2️⃣ Generate an explanation

But normally the pipeline only forwards ONE output.


------------------------------------------------------------
7️⃣ RunnablePassthrough Solution
------------------------------------------------------------

RunnablePassthrough()

This simply **forwards the incoming data unchanged**.

Think of it like:

identity(x) → x


------------------------------------------------------------
8️⃣ Parallel Chain
------------------------------------------------------------

parallel_chain = RunnableParallel({

    "joke": RunnablePassthrough(),

    "explanation":
        prompt2 → model → parser
})

Input to this stage:

"Why did the cricket go to the doctor..."


RunnableParallel does two things simultaneously:

Branch 1
--------
joke → passthrough

Result:
"Why did the cricket go to the doctor..."


Branch 2
--------
explanation → prompt2 → model → parser

Result:
Explanation text


Outputs merged into dictionary:

{
  "joke": "...",
  "explanation": "..."
}


------------------------------------------------------------
9️⃣ Final Chain
------------------------------------------------------------

chain = RunnableSequence(
    joke_gen_chain,
    parallel_chain
)


------------------------------------------------------------
🔟 Execution Flow
------------------------------------------------------------

Input

{"topic": "Cricket"}


STEP 1
------

Prompt1
↓
Model
↓
Parser

Result:

"Why did the cricket go to the doctor..."


STEP 2
------

Parallel stage

Branch A
--------
RunnablePassthrough

Output:
joke


Branch B
--------
Prompt2 → Model → Parser

Output:
explanation


STEP 3
------

Outputs combined


Final Result

{
  "joke": "...",
  "explanation": "..."
}


------------------------------------------------------------
11️⃣ Visual Pipeline
------------------------------------------------------------

Input
 │
 ▼
Prompt1
 │
 ▼
Model
 │
 ▼
Parser
 │
 ▼
Parallel
 ├───────────────┐
 ▼               ▼
Passthrough     Prompt2
 │               │
 │               ▼
 │             Model
 │               │
 │               ▼
 │             Parser
 └───────────────┘
        │
        ▼
Final Output


------------------------------------------------------------
12️⃣ Key Concept
------------------------------------------------------------

RunnablePassthrough is used when you want to:

• keep the original data
• forward it unchanged
• use it alongside new outputs

Common Use Cases:

• Keep original text + summary
• Keep question + answer
• Keep document + extracted metadata
• Keep prompt + model reasoning


------------------------------------------------------------
Final Output Example
------------------------------------------------------------

{
  "joke": "Why did the cricket go to the doctor?",
  "explanation": "The joke plays on the word 'pitch'..."
}
"""