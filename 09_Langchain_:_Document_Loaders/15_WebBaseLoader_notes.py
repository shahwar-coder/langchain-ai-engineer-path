import os
from langchain_community.document_loaders import WebBaseLoader

os.environ["USER_AGENT"] = "Mozilla/5.0"

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")

docs = loader.load()

print(len(docs))
print(docs[0].page_content[:500])