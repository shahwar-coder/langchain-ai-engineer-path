from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Load all PDF files from the 'books' directory
loader = DirectoryLoader(
    path='books',          # folder containing files
    glob='*.pdf',          # pattern to select only PDF files
    loader_cls=PyPDFLoader # loader used for each matched file
)

# Load documents (each page becomes a Document object)
docs = loader.load()

# Print content of the first page from the loaded documents
print(docs[0].page_content)

# Print metadata (source file path and page number)
print(docs[0].metadata)

'''
books/
 ├── book1.pdf
 ├── book2.pdf
 └── notes.txt

DirectoryLoader
      ↓
select files matching "*.pdf"
      ↓
PyPDFLoader loads each PDF
      ↓
List[Document] (each page = one Document)
'''