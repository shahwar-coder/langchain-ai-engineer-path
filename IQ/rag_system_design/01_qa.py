'''
1. How would you design a scalable RAG system for millions of documents?

Ans.
I would separate ingestion and query pipelines.
Use persistent vector storage with ANN indexing,
and horizontally scale retriever and LLM services independently.


2. How would you handle document updates in a production RAG system?

Ans.
Use incremental indexing.
Re-embed only changed documents instead of rebuilding the entire vector store.


3. How would you reduce latency in a RAG system?

Ans.
Optimize chunk size, use ANN indexes,
cache frequent queries,
and possibly stream LLM responses.


4. How would you design multi-tenant RAG (multiple clients)?

Ans.
Use namespace separation in vector DB.
Isolate embeddings per tenant while sharing infrastructure.


5. How would you handle very large documents (1000+ pages)?

Ans.
Implement hierarchical chunking.
Use metadata-based filtering before similarity search.


6. How would you evaluate RAG performance?

Ans.
Measure retrieval precision (are relevant chunks returned?)
and generation accuracy (is answer grounded and correct?).


7. What bottlenecks typically appear in RAG systems?

Ans.
Embedding computation during ingestion.
Vector search latency at scale.
LLM inference time.


8. How would you prevent hallucination in a RAG system?

Ans.
Strengthen grounding prompts,
limit answer scope to retrieved context,
and validate output against source chunks.


9. How would you design RAG for real-time systems?

Ans.
Precompute embeddings,
use persistent vector storage,
and deploy low-latency LLM inference endpoints.


10. How would you architect RAG for high availability?

Ans.
Use replicated vector databases,
stateless retriever services,
and load-balanced LLM inference nodes.
'''
