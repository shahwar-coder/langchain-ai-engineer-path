'''
RAG System Flow (Concise Explanation)

User query is first processed using semantic search,
which converts the query into an embedding and retrieves
meaningfully similar document pages from the database.

These retrieved pages are combined with the original
user query to form a structured system prompt.

This enriched prompt is then sent to the LLM (the "brain"),
which generates a context-aware response grounded in
the retrieved documents.

⭐ Core idea:
Retrieve relevant context first, then generate —
so answers are based on knowledge, not guesswork.
'''