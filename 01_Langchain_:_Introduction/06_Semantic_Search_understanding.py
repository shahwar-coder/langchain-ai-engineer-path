'''
Semantic Search (Diagram Explanation — Concise)

User question:
"How many runs has Virat scored?"

1️⃣ Embedding step
- Question → converted into a vector (e.g., 100D)
- Each paragraph (Virat, Bumrah, Rohit) also converted into vectors
- All vectors exist in the same embedding space

2️⃣ Vector comparison
- Query vector compared with paragraph vectors
- Similar meaning → smaller angle / higher cosine similarity

3️⃣ Nearest match
- Query vector is closest to "Paragraph about Virat Kohli"
- Other paragraphs (Bumrah, Rohit) are farther away

4️⃣ Retrieval
- Closest paragraph selected
- Passed to LLM for answer generation

⭐ Core idea:
Text → embedding vector → geometric similarity → retrieve most semantically aligned content.
'''