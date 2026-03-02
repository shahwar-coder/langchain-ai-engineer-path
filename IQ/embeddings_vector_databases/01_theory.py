'''
Embeddings & Vector Databases — Concise Explanation

An embedding is simply a list of floating-point numbers
(e.g., 384D, 768D, 1536D vectors).

You *can* store embeddings as Python lists.
But searching them requires:

- Comparing query vector with every stored vector
- Computing cosine similarity manually
- Performing O(N) linear scan

This does not scale beyond small datasets.

--------------------------------------------------

How Vector Databases Handle Embeddings

Vector DBs still store float arrays,
but in optimized numeric formats:

- float32 contiguous memory
- Binary storage
- Memory-mapped arrays
- SIMD-optimized computation

More importantly, they build special ANN indexes like:
- HNSW
- IVF
- PQ
- FAISS graphs

These enable:

Sublinear search (≈ O(log N))
instead of O(N) scanning.

--------------------------------------------------

Key Difference

Python List:
- Python object overhead
- No indexing
- Linear scan
- Not scalable

Vector DB:
- Dense numeric storage
- Graph-based ANN indexing
- Fast nearest neighbor retrieval
- Built for millions of vectors

--------------------------------------------------

Core Insight:

Vector databases are not special because they store vectors.
They are powerful because they retrieve nearest neighbors efficiently at scale.
'''
