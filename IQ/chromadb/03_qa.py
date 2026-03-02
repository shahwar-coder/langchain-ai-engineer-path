'''
TOP 10 INTERVIEW Q&A (VECTOR STORE + CHROMADB SECTION)

1. What is a vector database?
   - A database optimized for storing and searching embedding vectors.
   - Used for semantic similarity search.

2. What does Chroma store internally?
   - Embedding vectors, original document text, and metadata.

3. Why not store embeddings in a Python list?
   - Lists do not scale.
   - No optimized indexing or similarity search.

4. Does Chroma generate embeddings?
   - No.
   - Embeddings must be generated externally.

5. What is the relationship between embeddings and Chroma?
   - Embeddings convert text to vectors.
   - Chroma stores and searches those vectors.

6. What happens when retriever is called?
   - Query → embedding → similarity search → top matching chunks returned.

7. Why is chunking necessary before storing in Chroma?
   - Improves retrieval accuracy.
   - Keeps chunk size within LLM context limits.

8. Where does Chroma store data by default?
   - In-memory unless persistence is enabled.

9. What is similarity search?
   - Mathematical comparison of vectors (usually cosine similarity).

10. Is Chroma an LLM?
   - No.
   - It is a vector storage and retrieval system, not a language model.
'''
