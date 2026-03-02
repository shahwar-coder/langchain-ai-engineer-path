'''
The text splitter breaks large documents into smaller chunks
so they fit within the LLM’s context (token) limit.

If chunks are too large, the model cannot process them.
If chunks are too small, important context may be lost.

Overlap solves this by repeating a small portion of text
between adjacent chunks.

This ensures:
- Each chunk fits the model’s limit
- Meaning that spans across boundaries is preserved

In short:
Chunking handles size constraints,
overlap protects context continuity.
'''
