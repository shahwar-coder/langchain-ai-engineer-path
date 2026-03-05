"""
Pydantic Student Example
Demonstrates defaults, optional fields, validation, and usage
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
import json


# Student Model
class Student(BaseModel):

    name: str = Field(
        default="Rahul",
        description="Full name of the student"
    )

    age: Optional[int] = Field(
        default=None,
        description="Age of the student"
    )

    email: EmailStr = Field(
        description="Valid email address of the student"
    )

    cgpa: float = Field(
        default=5.0,
        gt=0,
        lt=10,
        description="CGPA of the student on a 0–10 scale"
    )


# Creating a Student
print("\nCreating Student Object")
print("────────────────────────")

student = Student(
    email="rahul@example.com",
    age=21,
    cgpa=8.3
)

print(student)


# Accessing Fields
print("\nAccessing Individual Fields")
print("───────────────────────────")

print("Name:", student.name)
print("Age:", student.age)
print("Email:", student.email)
print("CGPA:", student.cgpa)


# Convert to Dictionary
print("\nDictionary Representation")
print("────────────────────────")

student_dict = student.model_dump()

print(student_dict)


# Using the Dictionary
print("\nUsing the Dictionary")
print("────────────────────")

print("Student name from dict:", student_dict["name"])
print("Student CGPA from dict:", student_dict["cgpa"])


# Example: modify dictionary
student_dict["cgpa"] = 9.1
print("Updated CGPA in dict:", student_dict["cgpa"])



# Convert to JSON
print("\nJSON Representation")
print("──────────────────")

student_json = student.model_dump_json(indent=2)

print(student_json)


# Using the JSON
print("\nUsing the JSON")
print("──────────────")

# Convert JSON back to Python dictionary
json_data = json.loads(student_json)

print("Name from JSON:", json_data["name"])
print("Email from JSON:", json_data["email"])


# Creating Student Object
# ────────────────────────
# name='Rahul' age=21 email='rahul@example.com' cgpa=8.3

# Accessing Individual Fields
# ───────────────────────────
# Name: Rahul
# Age: 21
# Email: rahul@example.com
# CGPA: 8.3

# Dictionary Representation
# ────────────────────────
# {'name': 'Rahul', 'age': 21, 'email': 'rahul@example.com', 'cgpa': 8.3}

# Using the Dictionary
# ────────────────────
# Student name from dict: Rahul
# Student CGPA from dict: 8.3
# Updated CGPA in dict: 9.1

# JSON Representation
# ──────────────────
# {
#   "name": "Rahul",
#   "age": 21,
#   "email": "rahul@example.com",
#   "cgpa": 8.3
# }

# Using the JSON
# ──────────────
# Name from JSON: Rahul
# Email from JSON: rahul@example.com