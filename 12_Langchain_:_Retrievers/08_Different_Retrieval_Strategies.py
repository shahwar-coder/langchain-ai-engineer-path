"""
Common Retriever Types in LangChain
===================================

1. Similarity Retriever (Most Common)
-------------------------------------

Purpose:
Find documents most semantically similar to the query.

How it works:
Query → Embedding → Vector Similarity Search → Top-K Docs

Use case:
Standard RAG pipelines where we want the most relevant chunks.

Example:

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)



2. MMR Retriever (Diversity-Aware)
----------------------------------

MMR = Maximal Marginal Relevance

Purpose:
Return relevant documents while reducing duplicate or overly similar chunks.

How it works:
Balances relevance and diversity among results.

Use case:
When similarity search returns multiple nearly identical chunks.

Example:

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 4}
)



3. Hybrid Retrieval (Production Systems)
----------------------------------------

Purpose:
Combine keyword search + vector similarity search.

How it works:
BM25 keyword search + semantic vector search.

Use case:
Production-grade RAG where both exact keywords and semantic meaning matter.

Example concept:

Keyword Search (BM25)
        +
Vector Similarity Search
        ↓
Combined Ranked Results



4. Self-Query Retriever (Metadata Filtering)
--------------------------------------------

Purpose:
Automatically convert user query into metadata filters.

How it works:
LLM interprets the query and applies filters to the vector database.

Example query:
"Show players from Chennai Super Kings"

Converted internally to:

filter = {"team": "Chennai Super Kings"}

Use case:
When documents contain useful metadata fields.


Summary
-------

similarity  → default choice for most RAG systems
mmr         → reduces duplicate chunks
hybrid      → best for production systems
self-query  → powerful when metadata filtering is required
"""
# ======================
"""
Retriever Strategy → Memory Keyword → What it does

similarity       → relevance      → returns most similar documents
mmr              → diversity      → avoids duplicate / similar chunks
hybrid           → keyword+semantic → combines BM25 keyword + vector search
self_query       → metadata       → converts query into metadata filters
multi_query      → perspective    → generates multiple query variations
parent_document  → context        → retrieves small chunks but returns full doc
time_weighted    → freshness      → prioritizes recently used or recent docs
compression      → filtering      → removes irrelevant parts from retrieved docs
"""