'''
1. Why do we split documents before creating embeddings?

Ans.
LLMs have context limits, so sending entire documents is inefficient.
Smaller chunks improve retrieval precision and keep semantic meaning focused.

# Example
Instead of embedding a 20-page PDF at once,
we embed 1000-character chunks for better matching.


2. Why do we use chunk_overlap while splitting?

Ans.
Important information may sit near chunk boundaries.
Overlap ensures context continuity and prevents meaning loss.

# Example
If a definition starts at the end of one chunk,
overlap ensures it continues into the next.


3. Why not embed the entire PDF as a single vector?

Ans.
A single vector would represent the whole document broadly.
It would not help retrieve specific relevant sections accurately.

Retrieval works best when chunks are semantically focused.


4. What role does the embedding model play in this function?

Ans.
It converts text chunks into numeric vectors.
These vectors capture semantic meaning for similarity search.


5. Why is Chroma.from_documents used instead of manually storing vectors?

Ans.
It automatically stores chunks, embeddings, and builds an index.
This enables efficient similarity search later.


6. What exactly does create_vector_store return?

Ans.
It returns a vector store object.
This object contains stored vectors and retrieval capabilities.


7. How does this function prepare data for RAG?

Ans.
It transforms raw text into indexed embeddings.
This allows fast retrieval of relevant context when answering queries.


8. What would happen if chunk size is too large?

Ans.
Retrieval becomes less precise.
LLM context may overflow, and irrelevant information may be mixed.


9. What would happen if chunk size is too small?

Ans.
Meaning may become fragmented.
Retrieval may return incomplete context.


10. Why do we separate this logic into a function?

Ans.
It keeps ingestion logic modular.
This improves maintainability and makes the pipeline reusable.
'''
