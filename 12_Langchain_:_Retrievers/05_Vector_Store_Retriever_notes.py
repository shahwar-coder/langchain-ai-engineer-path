"""
Vector Store Retriever

A Vector Store Retriever in LangChain is the most common type of retriever.
It allows you to search and retrieve documents from a vector store based on
semantic similarity using vector embeddings.

How It Works

1. Documents are stored inside a vector store (for example: FAISS, Chroma, Weaviate).

2. Each document is converted into a dense vector using an embedding model.

3. When a user sends a query:
   • The query is also converted into a vector.
   • The retriever compares the query vector with stored vectors.
   • It returns the top-k most similar documents.
"""