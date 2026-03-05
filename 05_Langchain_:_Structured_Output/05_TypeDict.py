'''
TypedDict (Python Concept)

TypedDict is a way to define the expected structure of a
Python dictionary using type hints.

It specifies:
- what keys should exist
- what type of values they should contain

Think of it as a blueprint for a dictionary.

--------------------------------------------------

Example

from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

person: Person = {
    "name": "Nihish",
    "age": 35
}

This helps IDEs and type checkers understand the
expected structure of the dictionary.

--------------------------------------------------

Key Characteristics

1️⃣ Clear Structure
Defines the required keys and their value types.

2️⃣ Better Developer Experience
IDEs provide autocomplete, type hints, and static analysis.

3️⃣ Lightweight
Only requires Python's built-in typing module.

4️⃣ Useful for LLM Structured Output
Commonly used to define simple schemas when expecting
JSON-like responses from LLMs.

--------------------------------------------------

Limitations

TypedDict does NOT enforce validation at runtime.

Example:

person: Person = {
    "name": 123,
    "age": "35"
}

Python will still run without errors.
Type checking happens only during static analysis.

--------------------------------------------------

Comparison

TypedDict
- Defines dictionary structure
- No runtime validation
- Lightweight

Pydantic
- Defines data models
- Provides runtime validation
- Better for complex schemas

--------------------------------------------------

Summary

TypedDict defines the expected schema of a dictionary
using type hints, improving code clarity and tooling
support, but it does not validate data during execution.
'''