from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

# model
model = ChatOllama(model="llama3.2:1b")

# schema
class Review(TypedDict):

    name: Annotated[
        str,
        "Name of the reviewer extracted from the text."
    ]

    key_themes: Annotated[
        list[str],
        "List of key themes discussed in the review. Each theme must be 1–2 words only. "
        "Return 4–6 themes maximum."
    ]

    summary: Annotated[
        str,
        "Write a concise summary of the review in 1–2 sentences."
    ]

    sentiment: Annotated[
        Literal["positive", "negative", "neutral"],
        "Overall sentiment of the review. Must be exactly one of: positive, negative, neutral."
    ]

    pros: Annotated[
        Optional[list[str]],
        "List of advantages mentioned in the review. Each item must be a short phrase (max 5 words)."
    ]

    cons: Annotated[
        Optional[list[str]],
        "List of disadvantages mentioned in the review. Each item must be a short phrase (max 5 words)."
    ]


# structured model
structured_model = model.with_structured_output(Review)

# prompt
review_text = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse!
The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking,
or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W
fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it
often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp,
vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but
anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI
still comes with bloatware—why do I need five different Samsung apps for things Google already
provides? The $1,300 price tag is also a hard pill to swallow.

Review by Shahwar Alam Naqvi
"""

result = structured_model.invoke(review_text)

print("\nStructured Output")
print("─" * 40)

print("Type:")
print(type(result))

print("\nReviewer Name:")
print(result["name"])

print("\nKey Themes:")
for theme in result["key_themes"]:
    print("-", theme)

print("\nSummary:")
print(result["summary"])

print("\nSentiment:")
print(result["sentiment"])

print("\nPros:")
if result.get("pros"):
    for p in result["pros"]:
        print("-", p)

print("\nCons:")
if result.get("cons"):
    for c in result["cons"]:
        print("-", c)

# ====

# Structured Output
# ────────────────────────────────────────
# Type:
# <class 'dict'>

# Reviewer Name:
# Shahwar Alam Naqvi's Review of the Samsung Galaxy S24 Ultra

# Key Themes:
# - Processor and Performance
# - Battery Life
# - Camera Capabilities
# - Design and Comfort
# - Software and Bloatware

# Summary:
# The Samsung Galaxy S24 Ultra is a powerhouse device with impressive specs, but its design and size make it less comfortable to use one-handed. The $1,300 price tag also raises questions about the value for money.

# Sentiment:
# positive

# Pros:
# - Impressive performance and battery life
# - Stunning 200MP camera with good low-light performance

# Cons:
# - Uncomfortable one-handed use due to weight and size
# - Samsung's One UI comes with bloatware
# - $1,300 price tag is a hard pill to swallow


# ====


"""
STRUCTURED REVIEW EXTRACTION — CLEAN EXPLANATION
===============================================

GOAL
----
Turn a messy paragraph review into a clean structured dictionary
so programs can easily use the information.

Instead of returning free text, the LLM fills a structured schema.


------------------------------------------------------------
1️⃣ MODEL INITIALIZATION
------------------------------------------------------------

model = ChatOllama(model="llama3.2:1b")

This loads the local LLM through Ollama.


------------------------------------------------------------
2️⃣ DEFINE OUTPUT SCHEMA (TypedDict)
------------------------------------------------------------

class Review(TypedDict):
    name: str
    key_themes: list[str]
    summary: str
    sentiment: Literal["positive","negative","neutral"]
    pros: Optional[list[str]]
    cons: Optional[list[str]]

This tells the model exactly what the output should look like.

Expected structure:

{
  "name": str,
  "key_themes": list[str],
  "summary": str,
  "sentiment": "positive | negative | neutral",
  "pros": list[str] | None,
  "cons": list[str] | None
}


------------------------------------------------------------
3️⃣ WHAT Annotated DOES
------------------------------------------------------------

Annotated[str, "instruction"]

These strings act like **guidelines for the model**.

Example:

summary → "Write a concise summary in 1–2 sentences"

So the model understands:
• what the field means
• how to format the output


------------------------------------------------------------
4️⃣ WHY Literal IS USED
------------------------------------------------------------

Literal["positive","negative","neutral"]

This restricts sentiment to **only these values**.

The model should NOT output things like:
    "disappointed"
    "mixed"
    "happy"

Only:
    positive
    negative
    neutral


------------------------------------------------------------
5️⃣ WHY Optional IS USED
------------------------------------------------------------

Optional[list[str]]

Means the field can be:

list[str] OR None

Example:

{
 "pros": [...]
}

or

{
 "pros": None
}

This is useful when the review does not mention advantages or disadvantages.


------------------------------------------------------------
6️⃣ CREATE STRUCTURED MODEL
------------------------------------------------------------

structured_model = model.with_structured_output(Review)

This tells LangChain:

"Force the LLM output to match the Review schema."

Now the LLM behaves like a **data extractor**.


------------------------------------------------------------
7️⃣ MODEL INVOCATION
------------------------------------------------------------

result = structured_model.invoke(review_text)

Input:
Messy paragraph review.

Output:
Clean structured dictionary.


------------------------------------------------------------
8️⃣ EXAMPLE OUTPUT
------------------------------------------------------------

{
 "name": "Shahwar Alam Naqvi",
 "key_themes": [
     "Processor performance",
     "Battery life",
     "Camera quality",
     "Device size",
     "Software bloatware"
 ],
 "summary": "...",
 "sentiment": "positive",
 "pros": [...],
 "cons": [...]
}


------------------------------------------------------------
9️⃣ WHY THIS IS POWERFUL
------------------------------------------------------------

Without structured output:

LLM returns messy paragraphs.

Hard to:
• parse
• store
• analyze


With structured output:

You get clean machine-readable data.


Now you can:

✓ store in database
✓ analyze sentiment
✓ build dashboards
✓ run analytics
✓ build review summarization systems


------------------------------------------------------------
🔟 SIMPLE MENTAL MODEL
------------------------------------------------------------

Instead of telling the AI:

"Write anything you want"

You give it a **form to fill**:

Name: ______
Themes: ______
Summary: ______
Sentiment: ______
Pros: ______
Cons: ______

The AI fills the form.


------------------------------------------------------------
KEY TAKEAWAY
------------------------------------------------------------

with_structured_output() turns an LLM from:

    Text generator

into a:

    Structured data extractor
"""