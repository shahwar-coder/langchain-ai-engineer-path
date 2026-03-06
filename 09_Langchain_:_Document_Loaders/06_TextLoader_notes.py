"""
TextLoader

TextLoader is a simple and commonly used document loader in LangChain
that reads plain text (.txt) files and converts them into LangChain
Document objects.

Use Case:
Ideal for loading chat logs, scraped text, transcripts, code snippets,
or any plain text data into a LangChain pipeline.

Limitation:
Works only with .txt files.

Flow:
TXT file
   ↓
TextLoader
   ↓
Document Object
"""