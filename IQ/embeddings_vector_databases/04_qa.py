'''
1. Why do vector databases use float32 arrays instead of Python lists?

Ans.
Vector databases store embeddings as raw float32 numbers placed directly in memory.
Python lists store pointers to full Python float objects.

This makes float32 arrays much lighter and faster, especially when storing large numbers of embeddings.

# Example
A 1536-dimensional embedding:
- float32 array ≈ 6 KB
- Python list ≈ 40+ KB


2. What does “contiguous memory” mean and why is it important?

Ans.
Contiguous memory means values are stored back-to-back in RAM.
The CPU can read them sequentially without jumping between memory locations.

This improves cache efficiency and speeds up vector math operations.


3. Why are Python lists inefficient for large embedding workloads?

Ans.
Each number in a Python list is a full object,
not just a raw numeric value.

That extra object metadata and pointer storage
multiplies memory usage when dealing with large datasets.


4. How does memory layout affect cosine similarity computation?

Ans.
Cosine similarity depends on dot products between vectors.
Contiguous float32 arrays allow the CPU to process numbers efficiently in sequence.

Python lists require pointer chasing,
which slows down numerical computation.


5. What is SIMD and why does it matter in vector search?

Ans.
SIMD allows the CPU to apply one instruction to multiple numbers at once.
Dense float32 arrays make this possible.

This significantly speeds up large-scale similarity calculations.


6. Why is cache locality important in embedding search?

Ans.
CPUs are optimized for sequential memory access.
Contiguous arrays stay in cache longer and reduce memory fetch delays.

Pointer-based structures cause more cache misses,
which slows performance.


7. How does memory usage scale when storing millions of embeddings?

Ans.
With float32 storage, memory grows predictably and efficiently.
With Python lists, object overhead grows with every value stored.

At scale, this difference can mean gigabytes of extra memory usage.


8. Why are vector databases designed closer to the hardware level?

Ans.
They are optimized for numerical workloads and similarity search.
Using dense numeric storage allows them to leverage CPU-level optimizations.

This ensures stable performance even with very large datasets.


9. Is storing vectors the main advantage of vector databases?

Ans.
No. Storing vectors is straightforward.
The real advantage is retrieving nearest neighbors efficiently at scale.

The performance comes from optimized indexing and memory design.


10. When does efficient memory layout start to matter?

Ans.
It matters once you move beyond small experiments.
At tens or hundreds of thousands of embeddings, inefficient storage begins to impact both speed and memory significantly.
'''
