from pydantic import BaseModel

class Student(BaseModel):
    name: str

new_student = {
    'name': 44  # name should have been string
}

student = Student(**new_student)

print(student)

# pydantic_core._pydantic_core.ValidationError: 1 validation error for Student
# name
#   Input should be a valid string [type=string_type, input_value=44, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_type