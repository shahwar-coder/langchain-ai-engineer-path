'''
ANSWERS TO YOUR QUESTIONS (CHROMADB)

1. Where is ChromaDB physically present?
   - By default, Chroma runs in-memory inside your Python process.
   - If configured with a persist_directory, it stores data locally on disk as files.
   - It is not cloud unless you explicitly deploy it.

2. Does Chroma store chunk → vector mapping?
   - Yes.
   - It stores:
       • Original chunk text
       • Embedding vector of that chunk
       • Optional metadata
   - Internally: (vector, document, metadata) triples.

3. What advantages does ChromaDB give?
   - Fast semantic similarity search.
   - Efficient vector indexing (no brute-force scanning).
   - Easy retrieval integration with LangChain.
   - Scalable storage compared to manual Python lists.
   - Supports persistence (can save & reload vector data).

4. Does Chroma use embedding model internally?
   - No.
   - Chroma does NOT generate embeddings itself.
   - You provide embeddings (via OllamaEmbeddings).
   - Chroma only stores and searches vectors.
   - It does NOT call any LLM internally.
'''
