"""
Vector Store vs Vector Database

Vector Store

A Vector Store is a lightweight library or service used to store
embeddings (vectors) and perform similarity search.

It focuses mainly on:
• storing vectors
• indexing vectors
• retrieving similar vectors

Vector stores usually do not include full database capabilities
such as transactions, advanced query systems, or security layers.

They are best suited for:
• small to medium datasets
• experimentation and prototyping
• local RAG pipelines

Example:
FAISS – stores vectors and supports similarity search, but
you must manage persistence and scaling separately.


Vector Database

A Vector Database is a full database system designed specifically
for storing and querying vector embeddings at scale.

In addition to similarity search, it provides many database-level
features such as:

• distributed architecture for horizontal scaling
• persistence and durability (replication, backups)
• metadata storage and filtering
• authentication and security controls
• support for very large datasets

Vector databases are designed for:
• production systems
• large-scale AI applications
• millions or billions of embeddings

Examples:
Pinecone
Weaviate
Milvus
Qdrant


Key Difference

Vector Store:
A simpler tool focused mainly on storing vectors and performing
similarity search.

Vector Database:
A full production-ready database system built to manage vectors
with scalability, reliability, and advanced database features.
"""