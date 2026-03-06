from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel, Field

load_dotenv()

# model 
model = ChatOllama(
    model="mistral:7b",
    temperature=0
)

# parser 1
parser1 = StrOutputParser()

# pydantic schema (required as we need definite values/ structured values of sentiment)
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Give sentiment of the feedback")

# parser 2 (pydantic)
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# prompt
prompt1 = PromptTemplate(
    template="""
    Classify the sentiment of the following feedback text into positive or negative.\n
    {feedback} \n
    {format_instructions}
    """,
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

# classifier chain
classifier_chain = prompt1 | model | parser2

# prompt : to responsd to POS feedback
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

# prompt : to responsd to NEG feedback
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# branch chain
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser1),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser1),
    RunnableLambda(lambda x: "could not find sentiment")
)

# chain
chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'This is a beautiful phone'})

chain.get_graph().print_ascii()

print("\nResult:\n")
print(result)

#     +-------------+      
#     | PromptInput |      
#     +-------------+      
#             *            
#             *            
#             *            
#    +----------------+    
#    | PromptTemplate |    
#    +----------------+    
#             *            
#             *            
#             *            
#      +------------+      
#      | ChatOllama |      
#      +------------+      
#             *            
#             *            
#             *            
# +----------------------+ 
# | PydanticOutputParser | 
# +----------------------+ 
#             *            
#             *            
#             *            
#        +--------+        
#        | Branch |        
#        +--------+        
#             *            
#             *            
#             *            
#     +--------------+     
#     | BranchOutput |     
#     +--------------+     

# Result:

#  Dear Valued Customer,

# Thank you for taking the time to share your positive feedback with us. We are thrilled to hear that our services have met and exceeded your expectations. Your satisfaction is our top priority, and we are committed to providing exceptional service every step of the way.

# Your kind words serve as a testament to our team's hard work and dedication. We will continue to strive for excellence in all that we do, and we appreciate your continued support.

# If there is ever anything you need or if you have any suggestions for improvement, please don't hesitate to reach out. We value your input and are always looking for ways to improve our services.

# Once again, thank you for choosing us, and we look forward to serving you in the future.

# Best Regards,
# [Your Name]
# [Your Position]
# [Company Name]


# ======


"""
RUNNABLE BRANCH CHAIN (LANGCHAIN LCEL)
======================================

Goal
----
Build an AI workflow that:

1️⃣ Classifies feedback sentiment (positive / negative)
2️⃣ Routes the workflow based on the sentiment
3️⃣ Generates an appropriate response

This demonstrates **conditional AI pipelines** using RunnableBranch.


------------------------------------------------------------
1️⃣ Model
------------------------------------------------------------

model = ChatOllama(model="mistral:7b", temperature=0)

• LLM used for both classification and response generation
• temperature=0 → deterministic output


------------------------------------------------------------
2️⃣ Why We Need Structured Output
------------------------------------------------------------

The model must return EXACTLY:

positive
or
negative

If we let the model return free text like:

"Looks like positive feedback"

branch logic becomes unreliable.

So we enforce **structured output** using Pydantic.


------------------------------------------------------------
3️⃣ Pydantic Schema
------------------------------------------------------------

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"]

Purpose:
Force the model to return structured JSON like:

{
  "sentiment": "positive"
}


------------------------------------------------------------
4️⃣ Pydantic Output Parser
------------------------------------------------------------

parser2 = PydanticOutputParser(pydantic_object=Feedback)

Responsibilities:

• Instructs the model to return JSON
• Validates output
• Converts output into a Python object


Example returned object:

Feedback(sentiment="positive")


------------------------------------------------------------
5️⃣ Classification Prompt
------------------------------------------------------------

prompt1 = PromptTemplate(
    template="""
# Classify the sentiment of the following feedback.

# {feedback}

# {format_instructions}
"""
)

format_instructions = parser2.get_format_instructions()

These instructions tell the model to produce structured JSON.


------------------------------------------------------------
6️⃣ Classifier Chain
------------------------------------------------------------

classifier_chain = prompt1 | model | parser2


Flow:

Feedback Text
     ↓
PromptTemplate
     ↓
LLM
     ↓
Pydantic Parser
     ↓
Feedback(sentiment="positive")


Example output object:

Feedback(sentiment="positive")


------------------------------------------------------------
7️⃣ Response Prompts
------------------------------------------------------------

Positive Response Prompt:

prompt2
"Write an appropriate response to this positive feedback"


Negative Response Prompt:

prompt3
"Write an appropriate response to this negative feedback"


------------------------------------------------------------
8️⃣ RunnableBranch
------------------------------------------------------------

branch_chain = RunnableBranch(

    (lambda x: x.sentiment == "positive",
        prompt2 | model | parser1),

    (lambda x: x.sentiment == "negative",
        prompt3 | model | parser1),

    RunnableLambda(lambda x: "could not find sentiment")
)

RunnableBranch works like an **if-elif-else router**.

Logic:

IF sentiment == positive
    → generate positive response

ELIF sentiment == negative
    → generate negative response

ELSE
    → fallback message


------------------------------------------------------------
9️⃣ Why the Lambda Receives "x"
------------------------------------------------------------

The input to branch is the **Pydantic object** returned by classifier.

Example:

Feedback(sentiment="positive")

So:

x.sentiment


------------------------------------------------------------
🔟 Final Chain
------------------------------------------------------------

chain = classifier_chain | branch_chain


Pipeline:

User Feedback
      ↓
Sentiment Classifier
      ↓
Structured Output
      ↓
Conditional Router
      ↓
Generate Response


------------------------------------------------------------
11️⃣ Execution Example
------------------------------------------------------------

Input:

"This is a beautiful phone"


Step 1 — Classification

Model returns:

Feedback(sentiment="positive")


Step 2 — Branch Routing

Condition:

x.sentiment == "positive"


Step 3 — Positive Response Generated


------------------------------------------------------------
12️⃣ Visual Pipeline
------------------------------------------------------------

Feedback Text
      │
      ▼
PromptTemplate (Classifier)
      │
      ▼
LLM
      │
      ▼
PydanticOutputParser
      │
      ▼
Feedback(sentiment)
      │
      ▼
RunnableBranch
 ┌───────────────┐
 │               │
 ▼               ▼
Positive Path   Negative Path
 │               │
 ▼               ▼
Response Gen    Response Gen
 │               │
 └───────┬───────┘
         ▼
      Final Output


------------------------------------------------------------
Key Idea
------------------------------------------------------------

RunnableBranch enables **conditional AI pipelines**.

It allows LLM workflows to behave like normal program logic:

IF condition → run chain A  
ELSE → run chain B
"""