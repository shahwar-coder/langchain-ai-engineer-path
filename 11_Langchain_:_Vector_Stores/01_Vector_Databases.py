"""
Vector Stores

What is a Vector Store?

A Vector Store (Vector Database) is a database designed to store
embeddings (numerical vector representations of text, images, etc.)
and efficiently search them using similarity.

Instead of searching by exact words, vector stores search by meaning
using vector similarity.

Example:

Text → Embedding Model → Vector
"Black holes are dense objects in space"
→ [0.23, -0.11, 0.98, ...]

These vectors are stored in a Vector Store.


Examples of Vector Stores

• Chroma
• FAISS
• Pinecone
• Weaviate
• Milvus
• Qdrant


Why Do We Need Vector Stores?

Embeddings are high-dimensional vectors (often 768–3072 numbers).
To retrieve relevant information, we must perform similarity search
between vectors.

Vector stores are optimized for this task.

They allow systems like RAG to retrieve the most semantically
relevant chunks of information.


Core Features

• Efficient similarity search (cosine, dot product, euclidean)
• Vector indexing (HNSW, IVF, etc.)
• Metadata filtering
• Fast nearest-neighbor search
• Scalable storage for millions of vectors


Core Advantages

1. Semantic Search

Instead of keyword matching, vector stores retrieve information
based on meaning.

Example:
Query: "How do stars collapse?"
Result: Documents about black holes or supernovae.


2. Fast Retrieval

Vector indexes allow very fast nearest-neighbor searches,
even with millions of embeddings.


Why Embeddings Should Be Stored in Vector Databases
(not normal databases)

Traditional databases (SQL/NoSQL) are not optimized for
vector similarity search.

Problems with normal DBs:

• No vector indexing
• Similarity comparisons are slow
• Poor performance with high-dimensional data

Vector databases solve this by using specialized
Approximate Nearest Neighbor (ANN) indexes that make
semantic search fast and scalable.


Summary

Vector Stores are specialized databases designed to store
embeddings and perform fast similarity search, making them
essential for systems like semantic search and RAG pipelines.
"""