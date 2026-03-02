'''
Why Python Lists Are Not Suitable for Vector DB Indexing (Concise)

Python lists provide positional indexing (O(1) access like lst[i]),
but they do NOT provide similarity-based search indexing.

For embeddings:
To find nearest neighbors, a list requires
a full linear scan:

    for v in embeddings:
        compute cosine(q, v)

This is O(N) per query.

The list has:
- No spatial structure
- No neighbor relationships
- No clustering
- No distance-aware partitioning

It is only a container.

--------------------------------------------------

Vector Databases Build Search Indexes

Vector DBs create ANN index structures like:
- HNSW (graph-based)
- IVF (cluster-based)
- PQ (quantized partitions)

These:
- Organize vectors spatially
- Store similarity relationships
- Reduce search space
- Enable sublinear search (~O(log N))

--------------------------------------------------

Additional Performance Difference

Python lists:
- Store boxed Python float objects
- Use pointer indirection
- Non-contiguous memory
- No SIMD / BLAS optimization

Vector DBs:
- Store float32 contiguous arrays
- Enable hardware-accelerated math
- Cache-efficient computation

--------------------------------------------------

Core Distinction

Python list:
Container without search intelligence.

Vector DB:
Spatial index + ANN algorithm + optimized numeric engine.

The limitation of lists is not storage —
it is the absence of similarity search indexing.
'''
