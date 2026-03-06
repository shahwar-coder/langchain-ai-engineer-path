"""
PyPDFLoader

PyPDFLoader is a document loader in LangChain used to read content
from PDF files and convert each page into a separate Document object.

Each page of the PDF becomes one Document with the page text and
metadata such as page number and source file.

Example Output:

[
    Document(page_content="Text from page 1",
             metadata={"page": 0, "source": "file.pdf"}),

    Document(page_content="Text from page 2",
             metadata={"page": 1, "source": "file.pdf"}),

    ...
]

Limitation:
It uses the PyPDF library internally, which may not work well
with scanned PDFs or documents with complex layouts.
"""