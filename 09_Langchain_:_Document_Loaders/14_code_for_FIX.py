from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for doc in docs:
    print(doc.page_content)

"""
DOCUMENT LOADING WITH DIRECTORYLOADER (LANGCHAIN)
=================================================

Goal
----
Load multiple PDF documents from a folder and read their content
one document page at a time using lazy loading.


------------------------------------------------------------
1️⃣ Imports
------------------------------------------------------------

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

DirectoryLoader
• Loads multiple files from a directory.

PyPDFLoader
• Reads PDF files and converts each page into a Document object.


------------------------------------------------------------
2️⃣ DirectoryLoader Setup
------------------------------------------------------------

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

Explanation of parameters:

path="books"
• Folder containing the PDF files.

Example structure:

books/
   ai_book.pdf
   ml_book.pdf
   dl_book.pdf


glob="*.pdf"
• File filter pattern.
• Only files ending with ".pdf" will be loaded.

Examples of glob patterns:

"*.pdf"        → all pdf files
"*.txt"        → all text files
"report*.pdf"  → files starting with "report"


loader_cls=PyPDFLoader
• Specifies how each file should be loaded.
• Here we use PyPDFLoader to read PDF files.


------------------------------------------------------------
3️⃣ Lazy Loading
------------------------------------------------------------

docs = loader.lazy_load()

Important concept:

lazy_load() returns a GENERATOR.

This means:
• Documents are loaded one at a time
• Not all files are loaded into memory at once


Why this matters:

If you have large datasets like:

• 10GB of PDFs
• 1000 documents

Lazy loading prevents memory overflow.


------------------------------------------------------------
4️⃣ Iterating Through Documents
------------------------------------------------------------

for doc in docs:
    print(doc.page_content)

Each "doc" is a LangChain Document object.

Document structure:

Document(
    page_content="text of the page",
    metadata={
        "source": "books/ai_book.pdf",
        "page": 0
    }
)


------------------------------------------------------------
5️⃣ What Gets Printed
------------------------------------------------------------

doc.page_content

This prints the actual text extracted from the PDF page.


Example output:

Artificial Intelligence is the field of study that focuses on
building systems capable of performing tasks that normally
require human intelligence.

Machine learning is a subset of AI that enables systems
to learn from data.


------------------------------------------------------------
6️⃣ What doc Contains Internally
------------------------------------------------------------

doc.page_content
→ the text content

doc.metadata
→ metadata about the page


Example:

print(doc.metadata)

Output:

{
  "source": "books/ai_book.pdf",
  "page": 3
}


------------------------------------------------------------
7️⃣ Why This Loader Is Useful
------------------------------------------------------------

DirectoryLoader is commonly used in:

• RAG pipelines
• Document ingestion
• Knowledge base systems
• Vector database indexing


Typical pipeline:

Documents
    ↓
DirectoryLoader
    ↓
Text Splitter
    ↓
Embeddings
    ↓
Vector Database


------------------------------------------------------------
8️⃣ lazy_load() vs load()
------------------------------------------------------------

loader.load()

• Loads ALL documents into memory
• Returns a list


loader.lazy_load()

• Loads documents one by one
• Returns a generator
• Better for large datasets


------------------------------------------------------------
Key Takeaway
------------------------------------------------------------

DirectoryLoader + PyPDFLoader allows you to:

• Load multiple PDFs automatically
• Extract text page by page
• Process large document collections efficiently.
"""