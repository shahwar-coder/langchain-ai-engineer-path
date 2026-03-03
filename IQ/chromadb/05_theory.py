'''
Why Use Chroma.from_documents?

Chroma.from_documents() is a high-level ingestion helper.

It automatically:
- Takes document chunks
- Generates embeddings
- Stores (text + vector + metadata)
- Builds the similarity index

Instead of manually:
1. Embedding each chunk
2. Inserting vectors
3. Managing IDs
4. Building indexes

It handles the full pipeline in one step.

Result:
Documents are indexed and ready
for efficient similarity search.
'''
