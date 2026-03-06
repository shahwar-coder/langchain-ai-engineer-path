"""
Semantic Meaning–Based Text Splitting

Semantic meaning–based splitting divides text based on meaning
rather than fixed size or document structure.

The goal is to group sentences that talk about the same topic
and separate sentences that discuss different topics.

Example idea:

Text
    ↓
Sentences about farming
Sentences about cricket (IPL)
Sentences about terrorism

Each topic becomes its own chunk.

Benefits

• Keeps related ideas together in the same chunk.
• Prevents mixing unrelated topics inside one chunk.
• Produces cleaner embeddings.
• Improves retrieval accuracy in RAG systems.

Why It Is Useful

If a chunk contains multiple unrelated topics, embeddings
become noisy and search results become less accurate.

Semantic splitting ensures each chunk represents
one coherent idea.
"""