from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

# model
model = ChatOllama(model="llama3.2:1b")

# schema
class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review either negative, positive or neutral"]

# structured model
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to
other brands. Hoping for a software update to fix this.""")

print("\nStructured Output")
print("─" * 40)

print("Type:")
print(type(result))

print("\nSummary:")
print(result["summary"])

print("\nSentiment:")
print(result["sentiment"])

# Structured Output
# ────────────────────────────────────────
# Type:
# <class 'dict'>

# Summary:
# I can understand your frustration with the software's bloated feel and outdated UI

# Sentiment:
# disappointed


# ====


"""
STRUCTURED OUTPUT WITH LANGCHAIN — SIMPLE EXPLANATION
=====================================================

Goal of This Code
-----------------
Instead of letting the LLM return messy text,
we force it to return a **structured response**.

Example structure we want:

{
    "summary": "...",
    "sentiment": "..."
}

This makes LLM outputs easier to use in programs.


------------------------------------------------------------
1️⃣ Load Environment
------------------------------------------------------------

load_dotenv()

Loads environment variables if needed (API keys etc).
Not strictly required for local Ollama but good practice.


------------------------------------------------------------
2️⃣ Initialize the Model
------------------------------------------------------------

model = ChatOllama(model="llama3.2:1b")

This loads a local LLM through Ollama.


------------------------------------------------------------
3️⃣ Define the Expected Output Schema
------------------------------------------------------------

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review either negative, positive or neutral"]

TypedDict defines the **structure of the output dictionary**.

Expected output shape:

{
    "summary": str
    "sentiment": str
}

Annotated[str, "..."] adds **instructions for the model**.

Example meaning:

summary → "A brief summary of the review"
sentiment → "positive / negative / neutral"


------------------------------------------------------------
4️⃣ Convert the Model into a Structured Model
------------------------------------------------------------

structured_model = model.with_structured_output(Review)

This is the key line.

LangChain now tells the LLM:

    "Your response MUST follow the Review schema."

So the model is guided to return structured data.


------------------------------------------------------------
5️⃣ Invoke the Model
------------------------------------------------------------

result = structured_model.invoke(review_text)

Input:
A messy paragraph review.

Output:
A clean structured dictionary.


------------------------------------------------------------
6️⃣ Example Result
------------------------------------------------------------

{
    "summary": "I can understand your frustration with the software's bloated feel and outdated UI",
    "sentiment": "disappointed"
}

Type:

dict


------------------------------------------------------------
7️⃣ Why This Is Powerful
------------------------------------------------------------

Without structured output:

LLM might return messy text like:

"The review expresses frustration with bloated software and outdated UI..."

Hard to parse programmatically.


With structured output:

{
    "summary": "...",
    "sentiment": "..."
}

Now your code can easily:

✓ store it in databases  
✓ send to APIs  
✓ run analytics  
✓ build dashboards  


------------------------------------------------------------
8️⃣ Key Concept
------------------------------------------------------------

Normal LLM Output:
    Unstructured text

Structured LLM Output:
    Typed data (dict / JSON)


------------------------------------------------------------
9️⃣ Mental Model
------------------------------------------------------------

Think of it like giving the LLM a **form to fill**.

Instead of saying:
    "Write anything"

You say:
    "Fill this form"

Form:

Summary: ______  
Sentiment: ______  


------------------------------------------------------------
🔑 Final Takeaway
------------------------------------------------------------

`with_structured_output()` forces the LLM
to produce predictable structured data
instead of free-form text.

This is essential when building:

• AI pipelines
• AI APIs
• Data extraction systems
• Production AI applications
"""