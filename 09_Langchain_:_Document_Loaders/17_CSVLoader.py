from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='09_Langchain_:_Document_Loaders/students.csv')

data = loader.load()

print(data[0])

'''
I printed one of the document object -> equivalent to one row
'''

# Document(
#     page_content="""
# StudentID: 1
# Name: Aarav Sharma
# Age: 15
# Grade: 10
# City: Bangalore
# """,
#     metadata={
#         "source": "09_Langchain_:_Document_Loaders/students.csv",
#         "row": 0
#     }
# )