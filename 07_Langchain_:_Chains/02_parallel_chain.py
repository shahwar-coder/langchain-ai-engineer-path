'''
             Input
               │
               ▼
        RunnableParallel
         ┌─────────────┐
         │             │
         ▼             ▼
     Prompt1        Prompt2
         │             │
         ▼             ▼
       Model1        Model2
         │             │
         ▼             ▼
      Notes           Quiz
         └──────┬──────┘
                ▼
             Prompt3
                │
                ▼
              Model2
                │
                ▼
             Output
'''

from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# model 1
model1 = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)

# model 2
model2 = ChatOllama(
    model="mistral:7b",
    temperature=0
)

# prompts
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

# parser
parser = StrOutputParser()

# parallel chain
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

# merge chain
merge_chain = prompt3 | model2 | parser

# chain
chain = parallel_chain | merge_chain

# A paragraph about Antropic (example text)
text = """Anthropic is an artificial intelligence company focused on building safe and reliable AI systems. It was founded in 2021 by former researchers from OpenAI, including Dario Amodei and Daniela Amodei. The company is known for developing the Claude family of AI models, such as Claude, which are designed to be helpful, honest, and harmless. Anthropic focuses heavily on AI safety research, ensuring that advanced AI systems behave in ways that align with human values. One of its major research ideas is Constitutional AI, a method where AI models are trained to follow a set of guiding principles. The company has received significant investments from large technology firms like Amazon and Google. Anthropic competes with other AI organizations such as OpenAI and Google DeepMind. Their models are used for tasks like coding assistance, writing, research, and enterprise AI solutions. The company also publishes research on AI alignment and responsible AI development. Overall, Anthropic aims to build powerful AI systems that are both useful and safe for society."""

# execute
result = chain.invoke({'text': text})

# viz graph
print("\nChain Graph")
print('-'*40)
chain.get_graph().print_ascii()

# display
print("Result: ")
print('-'*40)
print(result)

# Chain Graph
# ----------------------------------------
#             +---------------------------+            
#             | Parallel<notes,quiz>Input |            
#             +---------------------------+            
#                  **               **                 
#               ***                   ***              
#             **                         **            
# +----------------+                +----------------+ 
# | PromptTemplate |                | PromptTemplate | 
# +----------------+                +----------------+ 
#           *                               *          
#           *                               *          
#           *                               *          
#   +------------+                    +------------+   
#   | ChatOllama |                    | ChatOllama |   
#   +------------+                    +------------+   
#           *                               *          
#           *                               *          
#           *                               *          
# +-----------------+              +-----------------+ 
# | StrOutputParser |              | StrOutputParser | 
# +-----------------+              +-----------------+ 
#                  **               **                 
#                    ***         ***                   
#                       **     **                      
#            +----------------------------+            
#            | Parallel<notes,quiz>Output |            
#            +----------------------------+            
#                           *                          
#                           *                          
#                           *                          
#                  +----------------+                  
#                  | PromptTemplate |                  
#                  +----------------+                  
#                           *                          
#                           *                          
#                           *                          
#                    +------------+                    
#                    | ChatOllama |                    
#                    +------------+                    
#                           *                          
#                           *                          
#                           *                          
#                 +-----------------+                  
#                 | StrOutputParser |                  
#                 +-----------------+                  
#                           *                          
#                           *                          
#                           *                          
#               +-----------------------+              
#               | StrOutputParserOutput |              
#               +-----------------------+              
# Result: 
# ----------------------------------------
#  Title: Anthropic: An Overview of the Artificial Intelligence Company

# Anthropic is an artificial intelligence (AI) company founded in 2021 by Dario Amodei and Daniela Amodei, former researchers from OpenAI. The company's primary focus is on building safe AI systems that prioritize AI safety research and use Constitutional AI method.

# **Key Points:**

# 1. **Company Overview**: Anthropic was established in 2021 with a mission to develop safe and beneficial AI systems.

# 2. **Founders**: The company is co-founded by Dario Amodei and Daniela Amodei, who previously worked at OpenAI.

# 3. **Products and Services**: Anthropic develops the Claude family of AI models, including Claude, designed to be helpful, honest, and harmless. These models are used for tasks such as coding assistance, writing, research, and enterprise AI solutions. Additionally, they publish research on AI alignment and responsible AI development.

# 4. **Research**: One of Anthropic's major research ideas is Constitutional AI, a method where AI models are trained to follow a set of guiding principles.

# 5. **Competition**: Anthropic competes with other prominent AI companies like OpenAI and Google DeepMind.

# 6. **Investments**: Significant investments have been made in Anthropic by large technology firms such as Amazon and Google.

# **Quiz:**

# 1. Who founded Anthropic?
#    - Anthropic was founded by Dario Amodei and Daniela Amodei in 2021.

# 2. What is Anthropic known for developing?
#    - Anthropic is known for developing the Claude family of AI models, such as Claude.

# 3. What is one of Anthropic's major research ideas?
#    - One of Anthropic's major research ideas is Constitutional AI.

# 4. Which large technology firms have invested in Anthropic?
#    - Anthropic has received significant investments from Amazon and Google.

# 5. What tasks are Anthropic's models used for?
#    - Anthropic's models are used for coding assistance, writing, research, and enterprise AI solutions, among other tasks. They also publish research on AI alignment and responsible AI development.


# ======


"""
PARALLEL CHAIN (LANGCHAIN LCEL) — CLEAR & ORGANIZED FLOW
========================================================

Goal
----
Process the same input text in TWO different ways simultaneously:

1️⃣ Generate notes
2️⃣ Generate quiz questions

Then combine both results into a single document.

This is done using RunnableParallel.


------------------------------------------------------------
1️⃣ Models
------------------------------------------------------------

model1 = ChatOllama("llama3.2:1b")
model2 = ChatOllama("mistral:7b")

Why two models?

model1 → generates NOTES  
model2 → generates QUIZ and FINAL MERGED OUTPUT


------------------------------------------------------------
2️⃣ Prompt Templates
------------------------------------------------------------

Prompt 1 → Notes Generator

"Generate short and simple notes from the following text"

Output:
Short explanatory notes.


Prompt 2 → Quiz Generator

"Generate 5 short question answers from the following text"

Output:
5 Q&A style questions.


Prompt 3 → Merge Prompt

"Merge notes and quiz into a single document"

This step combines both outputs.


------------------------------------------------------------
3️⃣ Output Parser
------------------------------------------------------------

parser = StrOutputParser()

Purpose:
Convert AIMessage objects into plain text so the next step
can easily consume them.


------------------------------------------------------------
4️⃣ RunnableParallel
------------------------------------------------------------

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser
})

RunnableParallel runs BOTH chains at the same time.

Input:
{
  "text": paragraph
}

Outputs:
{
  "notes": "...generated notes...",
  "quiz": "...generated quiz..."
}

Key Idea:
Both tasks run independently and simultaneously.


------------------------------------------------------------
5️⃣ Merge Chain
------------------------------------------------------------

merge_chain = prompt3 | model2 | parser

This step receives:

{
  "notes": "...",
  "quiz": "..."
}

And merges them into one final document.


------------------------------------------------------------
6️⃣ Final Chain
------------------------------------------------------------

chain = parallel_chain | merge_chain

Pipeline:

Input Text
    ↓
Parallel Processing
    ↓
Notes + Quiz
    ↓
Merge Step
    ↓
Final Document


------------------------------------------------------------
7️⃣ Execution Flow
------------------------------------------------------------

result = chain.invoke({"text": paragraph})

Step-by-step:

Step 1
ParallelChain receives text

Step 2
Two tasks run simultaneously:

   Branch 1:
      prompt1 → model1 → notes

   Branch 2:
      prompt2 → model2 → quiz

Step 3
Both results combine into:

{
  "notes": "...",
  "quiz": "..."
}

Step 4
merge_chain receives them

Step 5
prompt3 instructs model2 to merge them

Step 6
Final formatted document produced.


------------------------------------------------------------
8️⃣ Visual Pipeline
------------------------------------------------------------

Input Text
      │
      ▼
RunnableParallel
 ┌─────────────┐
 │             │
 ▼             ▼
Notes Chain   Quiz Chain
 │             │
 ▼             ▼
Notes         Quiz
      │
      ▼
 Merge Prompt
      │
      ▼
 Final Model
      │
      ▼
 Output Document


------------------------------------------------------------
9️⃣ Why Parallel Chains Are Powerful
------------------------------------------------------------

They allow you to:

✓ Run multiple AI tasks simultaneously
✓ Extract different insights from the same data
✓ Build multi-output AI pipelines
✓ Speed up processing

Common real-world use cases:

• Generate notes + flashcards
• Extract summary + keywords
• Create explanation + quiz
• Generate documentation + tests


------------------------------------------------------------
KEY TAKEAWAY
------------------------------------------------------------

RunnableParallel lets multiple LLM pipelines run
in parallel on the same input, producing multiple outputs
that can later be combined into a final result.
"""