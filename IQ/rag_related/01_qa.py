'''
1. What problem does RAG solve compared to using an LLM alone?

Ans.
LLMs generate answers based on training data, which may be outdated or incomplete.
RAG adds a retrieval step so answers are grounded in external documents.

This reduces hallucination and improves factual reliability.


2. Why do we separate retrieval and generation instead of fine-tuning the model?

Ans.
Fine-tuning changes model weights and is expensive.
Retrieval allows dynamic knowledge updates without retraining.

You can swap documents without touching the model.


3. What is the role of the retriever in a RAG pipeline?

Ans.
The retriever converts the query into an embedding.
It finds semantically similar chunks from the vector store.

It does not generate answers — it only selects context.


4. Why is chunking critical for RAG performance?

Ans.
Retrieval works best when chunks are focused and semantically tight.
If chunks are too large, irrelevant data is mixed.
If too small, meaning gets fragmented.


5. What happens if retrieval quality is poor?

Ans.
Even a powerful LLM cannot fix irrelevant context.
RAG accuracy heavily depends on good retrieval.


6. What is the difference between exact nearest neighbor and ANN?

Ans.
Exact search compares against all vectors.
ANN uses indexing structures for fast approximate results.

In large systems, ANN is necessary for performance.


7. Why is prompt structure important in RAG?

Ans.
The LLM must clearly understand what is context and what is question.
Poor prompt formatting can cause it to ignore or misuse retrieved data.


8. Why does RAG improve factual consistency?

Ans.
Because the model is constrained to answer using retrieved context.
It reduces reliance on memory and encourages grounding.


9. What are the two main components of RAG?

Ans.
Retriever (semantic search)
Generator (LLM reasoning over context)


10. When would RAG not be suitable?

Ans.
When answers require reasoning beyond available documents.
Or when latency requirements are extremely strict.
'''
