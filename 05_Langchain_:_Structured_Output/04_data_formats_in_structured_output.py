'''
Structured Output using with_structured_output (LangChain)

Normally when we call an LLM:

    result = model.invoke(prompt)

the model returns plain text.

If we want structured data (like JSON or objects),
LangChain provides:

    model.with_structured_output(schema)

This instructs the model to return results that follow
a predefined structure (schema).

--------------------------------------------------

Execution Flow

Prompt
  ↓
model.with_structured_output(schema)
  ↓
model.invoke()
  ↓
Structured Output

The returned result automatically follows the schema.

--------------------------------------------------

Ways to Define the Schema

LangChain supports three common schema formats.

1️⃣ TypedDict

A lightweight Python type definition.

Used for simple structures where validation is not required.

Example fields:
- product: str
- sentiment: float

Output is returned as a Python dictionary.

Best for:
Simple projects and quick structured outputs.

--------------------------------------------------

2️⃣ Pydantic Models

The most commonly used method in production.

Provides:
- strong typing
- validation
- required fields
- nested structures

Output is returned as a Pydantic object.

Best for:
Production systems, APIs, agents, and structured workflows.

--------------------------------------------------

3️⃣ JSON Schema

Schema defined using standard JSON schema format.

Useful for:
- API interoperability
- language-agnostic systems
- external schema definitions

Output is returned as JSON data matching the schema.

--------------------------------------------------

Schema Comparison

TypedDict
- Simple
- No validation
- Lightweight

Pydantic
- Strong typing
- Built-in validation
- Most commonly used

JSON Schema
- Standardized
- API friendly
- More verbose

--------------------------------------------------

Summary

with_structured_output() allows an LLM to return
machine-readable data instead of plain text by enforcing
a predefined schema such as TypedDict, Pydantic, or
JSON Schema.
'''