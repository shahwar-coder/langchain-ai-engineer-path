from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int = 18   # default value

student = Student(name="Rahul")

print(student)

# name='Rahul' age=18