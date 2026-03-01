from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Create embedding model
embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)

# Documents
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Generate embeddings for all documents
doc_vectors = embedding.embed_documents(documents)

print(doc_vectors)
print("Number of documents:", len(doc_vectors))
print("Vector length of first doc:", len(doc_vectors[0]))