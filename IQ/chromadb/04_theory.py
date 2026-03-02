'''
Chroma stores embedding vectors along with their associated
documents and metadata.

When vectors are added, Chroma builds a similarity index
(typically an HNSW-based ANN index) in the background.

This index is constructed during ingestion (as vectors are inserted),
so it is ready before query time.

At search time, Chroma does not scan all vectors.
Instead, it uses the pre-built ANN index to quickly
find the nearest neighbors.

In short:
Chroma = vector storage + automatically built similarity index
for fast retrieval.
'''
