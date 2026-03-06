"""
CSVLoader

CSVLoader is a document loader in LangChain used to load data
from CSV (Comma-Separated Values) files and convert each row
into a LangChain Document object.

Each row in the CSV becomes one Document, where the row values
are stored as text and the column names help structure the content.


Example Output

[
 Document(
   page_content="name: John, role: Engineer, experience: 5",
   metadata={"row": 0, "source": "employees.csv"}
 ),
 Document(
   page_content="name: Sarah, role: Manager, experience: 8",
   metadata={"row": 1, "source": "employees.csv"}
 )
]


When to Use

• When your data is stored in tabular format (CSV files).
• Useful for datasets like customer data, product catalogs,
  financial records, logs, etc.
• Good for RAG systems built on structured datasets.


Limitations

• Works only with CSV formatted files.
• Large CSV files may require chunking after loading.
• Complex nested data structures are not handled well.
"""