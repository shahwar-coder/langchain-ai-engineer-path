from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    'name': 'Rahul',
    'age': 35           # Code will run even if I give string '35' here
}

print(new_person)

# ====

"""
TYPEDDICT — WHAT IS HAPPENING HERE?
===================================

Your Code
---------
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    "name": "Rahul",
    "age": 35
}

print(new_person)


------------------------------------------------------------
1️⃣ What is TypedDict?
------------------------------------------------------------

TypedDict is used to describe the STRUCTURE of a dictionary.

It tells type checkers (like mypy, pyright, IDEs):

    "A dictionary of type Person must contain:
        - name → str
        - age  → int"

So it acts like a **schema for a dictionary**.


Example structure:

Person
{
    "name": str
    "age": int
}


------------------------------------------------------------
2️⃣ Important: TypedDict does NOT enforce types at runtime
------------------------------------------------------------

Python itself does NOT enforce this rule when the program runs.

This means the following will still run:

new_person: Person = {
    "name": "Rahul",
    "age": "35"   # string instead of int
}

Why?

Because TypedDict is only used for:
    ✔ static type checking
    ✔ IDE hints
    ✔ code validation tools


------------------------------------------------------------
3️⃣ Static vs Runtime Checking
------------------------------------------------------------

Static Checking (before running code):

Tools like:
    mypy
    pyright
    pylance

will warn:

    age expected int but got str


Runtime Checking (when Python executes code):

Python ignores TypedDict completely.


------------------------------------------------------------
4️⃣ Why TypedDict is Still Useful
------------------------------------------------------------

TypedDict improves:

✓ Code readability  
✓ IDE autocomplete  
✓ Static error detection  
✓ Clear API contracts  
✓ Safer large codebases


Example:

Without TypedDict

    person = {"name": "Rahul", "age": 35}

We don't know the expected structure.


With TypedDict

    Person
    {
        name: str
        age: int
    }

Now the structure is clearly defined.


------------------------------------------------------------
5️⃣ Key Takeaway
------------------------------------------------------------

TypedDict defines the expected structure of a dictionary.

BUT:

    It is NOT runtime validation.

It is only for:

    Static type checking tools.


------------------------------------------------------------
6️⃣ If You Want Runtime Validation
------------------------------------------------------------

Use libraries like:

    Pydantic
    dataclasses
    attrs

Example (Pydantic):

class Person(BaseModel):
    name: str
    age: int

Person(name="Rahul", age="35")

Pydantic will convert "35" → 35 or raise an error.
"""