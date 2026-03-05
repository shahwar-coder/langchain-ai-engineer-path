from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal, List

load_dotenv()

# model
model = ChatOllama(model="llama3.2:1b")


# schema (Pydantic Model)
class Review(BaseModel):

    name: str = Field(
        description="Name of the reviewer extracted from the text."
    )

    key_themes: List[str] = Field(
        description="List of key themes discussed in the review. Each theme must be 1–2 words only. Return 4–6 themes."
    )

    summary: str = Field(
        description="Write a concise summary of the review in 1–2 sentences."
    )

    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Overall sentiment of the review."
    )

    pros: Optional[List[str]] = Field(
        default=None,
        description="List of advantages mentioned in the review. Each item must be a short phrase (max 5 words)."
    )

    cons: Optional[List[str]] = Field(
        default=None,
        description="List of disadvantages mentioned in the review. Each item must be a short phrase (max 5 words)."
    )


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
print(result.name)


print("\nKey Themes:")
for theme in result.key_themes:
    print("-", theme)


print("\nSummary:")
print(result.summary)


print("\nSentiment:")
print(result.sentiment)


print("\nPros:")
if result.pros:
    for p in result.pros:
        print("-", p)


print("\nCons:")
if result.cons:
    for c in result.cons:
        print("-", c)


# Type:
# <class '__main__.Review'>

# Reviewer Name:
# Shahwar Alam Naqvi

# Key Themes:
# - Tech Review
# - Samsung Galaxy S24 Ultra
# - Camera Performance

# Summary:
# The Samsung Galaxy S24 Ultra is a powerful smartphone with impressive specs, but its design and user experience could be improved. The camera performance is one of the standout features, especially in low light conditions.

# Sentiment:
# neutral

# Pros:
# - Impressive specs
# - Powerful processor
# - Fast charging
# - Excellent 200MP camera

# Cons:
# - Uncomfortable weight and size
# - Samsung's One UI bloatware
# - $1,300 price tag


# ====


"""
STRUCTURED OUTPUT WITH PYDANTIC (LangChain + Ollama)
====================================================

Goal
----
Convert a long, messy review paragraph into a clean, structured object
that your program can safely use.

Instead of getting random text from the LLM, we force it to produce
data that matches a predefined schema.


------------------------------------------------------------
1️⃣ Model Initialization
------------------------------------------------------------

model = ChatOllama(model="llama3.2:1b")

Loads the local LLM through Ollama.


------------------------------------------------------------
2️⃣ Define the Schema using Pydantic
------------------------------------------------------------

class Review(BaseModel):

Pydantic models define the exact structure the output must follow.

Expected output shape:

Review(
    name: str
    key_themes: List[str]
    summary: str
    sentiment: "positive | negative | neutral"
    pros: Optional[List[str]]
    cons: Optional[List[str]]
)


------------------------------------------------------------
3️⃣ Field() Descriptions
------------------------------------------------------------

Field(description="...")

These descriptions guide the LLM on how to fill each field.

Example:

summary = Field(
    description="Write a concise summary in 1–2 sentences"
)

This helps the model produce cleaner and more predictable outputs.


------------------------------------------------------------
4️⃣ Literal Restriction
------------------------------------------------------------

sentiment: Literal["positive", "negative", "neutral"]

This restricts sentiment to exactly those values.

The model should NOT produce:
    "happy"
    "mixed"
    "disappointed"

Only:
    positive
    negative
    neutral


------------------------------------------------------------
5️⃣ Optional Fields
------------------------------------------------------------

pros: Optional[List[str]]
cons: Optional[List[str]]

Means these fields can be:

List[str] OR None

If the review does not mention pros or cons,
the model can return None.


------------------------------------------------------------
6️⃣ Convert Model to Structured Mode
------------------------------------------------------------

structured_model = model.with_structured_output(Review)

This tells LangChain:

"Make the LLM return data matching the Review schema."


------------------------------------------------------------
7️⃣ Invoke the Model
------------------------------------------------------------

result = structured_model.invoke(review_text)

Input:
A messy multi-paragraph review.

Output:
A structured Review object.


------------------------------------------------------------
8️⃣ Result Type
------------------------------------------------------------

print(type(result))

Output:

<class '__main__.Review'>

Unlike the TypedDict version,
this returns a real **Pydantic object**, not a plain dictionary.


------------------------------------------------------------
9️⃣ Accessing Fields
------------------------------------------------------------

Because result is a Pydantic object, we use dot notation:

result.name
result.summary
result.sentiment
result.key_themes


------------------------------------------------------------
🔟 Why Pydantic Version is Better
------------------------------------------------------------

Compared to TypedDict:

TypedDict:
    - Only static typing
    - Returns plain dict

Pydantic:
    - Runtime validation
    - Stronger type guarantees
    - Object-like access
    - Better error handling


------------------------------------------------------------
Mental Model
------------------------------------------------------------

You give the AI a structured form to fill.

Form:

Reviewer Name: ______
Key Themes: ______
Summary: ______
Sentiment: ______
Pros: ______
Cons: ______

The model reads the review text and fills the form.


------------------------------------------------------------
Key Takeaway
------------------------------------------------------------

Using Pydantic + with_structured_output():

LLM becomes a structured data extractor
instead of just a free-form text generator.
"""