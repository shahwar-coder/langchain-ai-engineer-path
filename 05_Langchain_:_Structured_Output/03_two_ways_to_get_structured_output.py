'''
Two Ways to Get Structured Output in LangChain

LLMs differ in their ability to return structured data.
Some models can natively produce structured responses,
while others require parsing.

--------------------------------------------------

1️⃣ Models That Support Structured Output
(using with_structured_output)

Some modern models (e.g., GPT-4, Claude, Gemini)
can directly return outputs that match a defined schema.

LangChain provides:

    llm.with_structured_output(schema)

You define a schema (often using Pydantic), and the
model returns data that conforms to that structure.

Flow:

LLM → structured object → program

Advantages:
- High reliability
- Built-in validation
- No manual parsing required

--------------------------------------------------

2️⃣ Models That Do NOT Support Structured Output
(using Output Parsers)

Many models (especially smaller or open-source ones)
cannot guarantee structured responses.

In this case:
1. The prompt instructs the model to return JSON.
2. An Output Parser converts the text response into
   structured data.

Flow:

LLM → JSON text → Output Parser → structured data

Advantages:
- Works with any model
- Flexible fallback method

Limitations:
- Model may occasionally break the format.

--------------------------------------------------

Summary

LangChain provides two approaches:

- with_structured_output → for models that natively
  support structured responses.

- Output Parsers → for models that return text and
  need to be converted into structured data.
'''