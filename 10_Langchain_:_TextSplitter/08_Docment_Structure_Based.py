from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# text
text='''
class Student:
    
    def __init__(self, student_id, name, age, grade, city):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.city = city

    def display_info(self):
        """Print student details"""
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"City: {self.city}")

    def is_teenager(self):
        """Check if student is a teenager"""
        return 13 <= self.age <= 19

    def update_city(self, new_city):
        """Update student's city"""
        self.city = new_city

    def promote(self):
        """Promote student to next grade"""
        self.grade += 1

    def __str__(self):
        """Readable string representation"""
        return f"Student({self.student_id}, {self.name}, Grade {self.grade})"


# Example usage
student1 = Student(1, "Aarav Sharma", 15, 10, "Bangalore")

student1.display_info()
print("Teenager:", student1.is_teenager())

student1.promote()
print("After promotion:", student1.grade)

student1.update_city("Mumbai")
print("New city:", student1.city)
'''

# initialize splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

# now use splitter to split -> into chunks
chunks = splitter.split_text(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, 1):
    print(f"CHUNK {i}")
    print('-'*20)
    print(f"{chunk}") 


# Total Chunks: 5
# CHUNK 1
# --------------------
# class Student:
    
#     def __init__(self, student_id, name, age, grade, city):
#         self.student_id = student_id
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.city = city
# CHUNK 2
# --------------------
# def display_info(self):
#         """Print student details"""
#         print(f"ID: {self.student_id}")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Grade: {self.grade}")
#         print(f"City: {self.city}")
# CHUNK 3
# --------------------
# def is_teenager(self):
#         """Check if student is a teenager"""
#         return 13 <= self.age <= 19

#     def update_city(self, new_city):
#         """Update student's city"""
#         self.city = new_city
# CHUNK 4
# --------------------
# def promote(self):
#         """Promote student to next grade"""
#         self.grade += 1

#     def __str__(self):
#         """Readable string representation"""
#         return f"Student({self.student_id}, {self.name}, Grade {self.grade})"
# CHUNK 5
# --------------------
# # Example usage
# student1 = Student(1, "Aarav Sharma", 15, 10, "Bangalore")

# student1.display_info()
# print("Teenager:", student1.is_teenager())

# student1.promote()
# print("After promotion:", student1.grade)

# student1.update_city("Mumbai")
# print("New city:", student1.city)