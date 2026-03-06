from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel, Field

load_dotenv()

# model
model = ChatOllama(
    model='mistral:7b',
    temperature=0
    )

# pydantic schema
class Summary(BaseModel):
    summary: str = Field(description="5 line summary of the report")

# pydantic parser for summary
summary_parser = PydanticOutputParser(pydantic_object=Summary)

# string parser for report
report_parser = StrOutputParser()

# prompt template (report)
template_report = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# prompt template (summary)
template_summary = PromptTemplate(
    template="""
Write a 5 line summary of the following report.

{report}

{format_instructions}
""",
    input_variables=["report"],
    partial_variables={
        "format_instructions": summary_parser.get_format_instructions()
    }
)

# == chains ==
# Step 1: Report generation
report_chain = template_report | model | report_parser

# Step 2: Summary generation (structured output)
summary_chain = template_summary | model | summary_parser

# do this if no viz required
# report = report_chain.invoke({"topic": "Black Hole"})
# result = summary_chain.invoke({"report": report})
# else
# combine chains (for graph visualization)
chain = (
    report_chain
    | RunnableLambda(lambda report: {"report": report})
    | summary_chain
)

# visualize chain graph
print("\nChain Graph (ASCII)")
print("-" * 40)

chain.get_graph().print_ascii()


# execute chain
result = chain.invoke({"topic": "Black Hole"})


# display results
print("\nStructured Output")
print("-" * 40)
print(result)

print("\nSummary Text")
print("-" * 40)
print(result.summary)


# Chain Graph (ASCII)
# ----------------------------------------
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
#   +-----------------+    
#   | StrOutputParser |    
#   +-----------------+    
#             *            
#             *            
#             *            
#        +--------+        
#        | Lambda |        
#        +--------+        
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
#       +---------+        
#       | Summary |        
#       +---------+ 

# Structured Output
# ----------------------------------------
# summary="Black holes are regions in space where gravity is so strong that nothing, not even light, can escape. They form from massive stars' remnants and have three types: stellar, supermassive, and intermediate-mass. Evidence for their existence comes from star orbits, X-ray emissions, and gravitational waves. Black holes play a crucial role in understanding gravity, the universe structure, and star life cycle."

# Summary Text
# ----------------------------------------
# Black holes are regions in space where gravity is so strong that nothing, not even light, can escape. They form from massive stars' remnants and have three types: stellar, supermassive, and intermediate-mass. Evidence for their existence comes from star orbits, X-ray emissions, and gravitational waves. Black holes play a crucial role in understanding gravity, the universe structure, and star life cycle.


# =====


"""
MULTI-STEP LANGCHAIN PIPELINE WITH STRUCTURED OUTPUT
====================================================

Goal
----
Build a 2-stage AI pipeline:

1️⃣ Generate a detailed report about a topic
2️⃣ Convert that report into a structured 5-line summary

Instead of returning messy text, the final output is a
validated Pydantic object.


------------------------------------------------------------
1️⃣ Model Initialization
------------------------------------------------------------

model = ChatOllama(
    model="mistral:7b",
    temperature=0
)

• Uses local Ollama model
• temperature=0 → deterministic output
• Good for structured tasks


------------------------------------------------------------
2️⃣ Define the Structured Schema
------------------------------------------------------------

class Summary(BaseModel):
    summary: str

This defines the shape of the final output.

Expected result:

Summary(
    summary="5 line explanation..."
)


------------------------------------------------------------
3️⃣ Output Parsers
------------------------------------------------------------

report_parser = StrOutputParser()

Purpose:
Extract plain text from the model's response.

Model normally returns:
AIMessage(content="...")

StrOutputParser converts it to:

"...plain text..."


------------------------------------------------------------

summary_parser = PydanticOutputParser(pydantic_object=Summary)

Purpose:
Force the model to return data matching the Summary schema.

If the output does not match the schema → validation fails.


------------------------------------------------------------
4️⃣ Report Prompt Template
------------------------------------------------------------

template_report = PromptTemplate(
    template="Write a detailed report on {topic}",
)

Example prompt created:

"Write a detailed report on Black Hole"


------------------------------------------------------------
5️⃣ Summary Prompt Template
------------------------------------------------------------

template_summary = PromptTemplate(
    template="""
# Write a 5 line summary of the following report.

# {report}

# {format_instructions}
"""
)

Important part:

{format_instructions}

This comes from:

summary_parser.get_format_instructions()


Example instructions injected into prompt:

Return output as JSON:

{
  "summary": "..."
}

This helps the model produce valid structured output.


------------------------------------------------------------
6️⃣ First Chain: Report Generation
------------------------------------------------------------

report_chain = template_report | model | report_parser

Flow:

topic
  ↓
PromptTemplate
  ↓
ChatOllama
  ↓
StrOutputParser
  ↓
Plain text report


------------------------------------------------------------
7️⃣ Second Chain: Summary Generation
------------------------------------------------------------

summary_chain = template_summary | model | summary_parser

Flow:

report text
  ↓
PromptTemplate
  ↓
ChatOllama
  ↓
PydanticOutputParser
  ↓
Summary object


------------------------------------------------------------
8️⃣ RunnableLambda Bridge
------------------------------------------------------------

RunnableLambda(lambda report: {"report": report})

Why this exists:

report_chain outputs:

"long report text"

But summary_chain expects:

{"report": "long report text"}

So this lambda converts:

text
→
{"report": text}


------------------------------------------------------------
9️⃣ Combined Chain
------------------------------------------------------------

chain = (
    report_chain
    | RunnableLambda(lambda report: {"report": report})
    | summary_chain
)

Full pipeline:

topic
 ↓
generate report
 ↓
convert text → dict
 ↓
generate structured summary


------------------------------------------------------------
🔟 Visual Chain Graph
------------------------------------------------------------

PromptInput
   ↓
PromptTemplate (report)
   ↓
ChatOllama
   ↓
StrOutputParser
   ↓
Lambda
   ↓
PromptTemplate (summary)
   ↓
ChatOllama
   ↓
PydanticOutputParser
   ↓
Summary object


------------------------------------------------------------
11️⃣ Execution
------------------------------------------------------------

result = chain.invoke({"topic": "Black Hole"})

Steps internally:

1. Write report about black holes
2. Convert report → summary prompt
3. Model generates JSON summary
4. Pydantic validates it
5. Return Summary object


------------------------------------------------------------
12️⃣ Accessing Output
------------------------------------------------------------

print(result)

Summary(summary="...")

print(result.summary)

Outputs the actual text.


------------------------------------------------------------
KEY ARCHITECTURE IDEA
------------------------------------------------------------

This pipeline demonstrates:

Prompt → Model → Parser → Prompt → Model → Structured Data

You are chaining multiple AI steps together
to build a reliable workflow.


------------------------------------------------------------
MENTAL MODEL
------------------------------------------------------------

User Topic
   ↓
AI writes full report
   ↓
AI reads report
   ↓
AI produces structured summary
   ↓
Program receives validated data


------------------------------------------------------------
WHY THIS PATTERN IS POWERFUL
------------------------------------------------------------

This architecture is used in:

✓ AI data extraction systems
✓ AI report pipelines
✓ RAG summarization
✓ AI agents
✓ document processing systems

It turns LLMs into **data pipelines**, not just chatbots.
"""