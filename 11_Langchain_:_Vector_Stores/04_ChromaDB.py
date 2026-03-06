"""
Chroma Vector Store

Chroma is a lightweight, open-source vector database designed
for storing embeddings and performing fast similarity search.
It is especially popular for local development and small-to-
medium scale production RAG applications.

Chroma stores document embeddings and allows semantic search
to retrieve the most relevant pieces of information based on
vector similarity.

Hierarchy in Chroma

Tenant
  ↓
Database
  ↓
Collection
  ↓
Documents

• Tenant → Top level workspace (used for multi-user separation)
• Database → Logical grouping of collections
• Collection → Similar to a table that stores embeddings
• Documents → Actual stored text chunks with embeddings

Why Chroma is Popular

• Easy to set up and run locally
• Open-source
• Built for AI and RAG pipelines
• Fast similarity search
• Supports metadata filtering

Typical Use Case

Documents → Chunking → Embeddings → Stored in Chroma
User Query → Embedding → Similarity Search → Relevant Chunks Returned
"""