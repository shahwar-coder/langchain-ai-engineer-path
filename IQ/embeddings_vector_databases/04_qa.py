'''
REAL INDUSTRY INTERVIEW QUESTIONS — FLOAT32 CONTIGUOUS MEMORY

1. Why is float32 preferred over Python float objects for embeddings?
   - float32 uses 4 bytes per value; Python floats are full objects (~24–28 bytes).
   - Problem solved: drastically reduces memory footprint at scale.

2. What does "contiguous memory layout" mean and why is it important?
   - Data stored back-to-back in RAM.
   - Problem solved: enables cache-friendly and fast numerical computation.

3. How does contiguous memory improve CPU cache utilization?
   - Sequential access reduces cache misses.
   - Example: dot product reads memory linearly instead of chasing pointers.

4. Why are Python lists inefficient for large numerical workloads?
   - They store pointers to Python objects (object indirection).
   - Problem: poor cache locality and high memory overhead.

5. What is SIMD and why does contiguous float32 enable it?
   - SIMD executes one instruction on multiple data points at once.
   - Problem solved: accelerates vector math like cosine similarity.

6. How does memory layout affect cosine similarity computation?
   - Contiguous float arrays allow vectorized dot products.
   - Python lists require slower element-by-element access.

7. What is the memory impact difference at embedding scale (e.g., 1536D)?
   - Python list ≈ 40+ KB vs float32 array ≈ 6 KB.
   - At millions of vectors, this becomes terabytes vs gigabytes.

8. Why do vector databases use dense numeric storage internally?
   - To minimize overhead and maximize hardware-level optimization.
   - Problem solved: scalable storage and high-speed retrieval.

9. What performance bottleneck does object indirection create?
   - CPU must follow pointers, increasing cache misses.
   - Result: slower similarity search.

10. What is the core systems insight behind vector database efficiency?
   - Speed comes from hardware-aligned design:
     dense float32 storage + contiguous layout + SIMD + ANN indexing.
   - Not abstraction, but low-level memory and compute optimization.
'''
