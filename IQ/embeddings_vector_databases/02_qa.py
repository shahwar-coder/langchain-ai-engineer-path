'''
INTERVIEW QUESTIONS — EMBEDDINGS & VECTOR DATABASES

1. What is an embedding?
   - A dense vector (e.g., 768 floats) representing semantic meaning.
   - Problem solved: converts text into numeric form so similarity can be computed.

2. Can embeddings be stored in a Python list?
   - Yes, but retrieval requires manual cosine similarity over all vectors.
   - Problem: O(N) linear scan does not scale.

3. Why is linear search over embeddings not scalable?
   - Each query compares against every stored vector.
   - For 1M vectors, that means 1M similarity computations per query.

4. What makes a vector database different from a Python list?
   - It builds ANN indexes (e.g., HNSW) for fast nearest neighbor search.
   - Problem solved: reduces search complexity from O(N) to ~O(log N).

5. What is ANN (Approximate Nearest Neighbor)?
   - An algorithm that finds very close matches efficiently, not exact brute-force.
   - Trade-off: tiny accuracy loss for massive speed gain.

6. Why are embeddings stored in float32 contiguous memory?
   - Enables SIMD and optimized numeric computation.
   - Problem solved: reduces memory overhead and increases computation speed.

7. What is HNSW and why is it used?
   - A graph-based ANN index structure.
   - Problem solved: fast nearest neighbor search at large scale.

8. Why are vector databases suitable for millions of embeddings?
   - They use optimized storage + indexed search structures.
   - Python lists lack indexing and numeric optimization.

9. What is the core advantage of a vector database?
   - Efficient nearest neighbor retrieval at scale.
   - Not storage — retrieval efficiency.

10. When would a simple Python list be acceptable?
   - Very small datasets (e.g., <1000 vectors).
   - Beyond that, performance degrades rapidly.
'''
