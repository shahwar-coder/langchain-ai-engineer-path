"""
Multi-Query Retriever

A Multi-Query Retriever improves retrieval by generating multiple
different versions of the user's query before searching the vector store.

Problem with a single query
---------------------------
Sometimes one query does not capture all the ways information is written
in the documents. As a result, relevant documents may be missed.

Example query

User query:
"How can I stay healthy?"

This query could mean multiple things such as:
• What should I eat?
• How often should I exercise?
• How can I manage stress?

A simple similarity search might only match documents containing
the word "healthy" and miss documents discussing diet, exercise,
or mental wellness.


How Multi-Query Retrieval Works
-------------------------------

Step 1 — Start with the original user query.

Query:
"How can I stay healthy?"

Step 2 — An LLM generates multiple related queries that represent
different perspectives of the same question.

Generated queries:

1. "What are the best foods to maintain good health?"
2. "How often should I exercise to stay fit?"
3. "What lifestyle habits improve mental and physical wellness?"
4. "How can I boost my immune system naturally?"
5. "What daily routines support long-term health?"

Step 3 — Each generated query is sent to the vector database
to retrieve relevant documents.

Step 4 — All retrieved results are combined and duplicate
documents are removed.

Final result:
A broader and more complete set of documents covering
diet, exercise, mental health, and daily habits.


Why Multi-Query Retrieval is Useful
-----------------------------------

• Improves recall by exploring multiple query variations
• Reduces the chance of missing relevant documents
• Captures different ways information may be written
• Works well when documents use varied language


Mental Model
------------

Single Query Retrieval
Query → Vector Search → Results

Multi-Query Retrieval
Query
  ↓
LLM generates multiple query variations
  ↓
Multiple vector searches
  ↓
Merge + deduplicate results
"""