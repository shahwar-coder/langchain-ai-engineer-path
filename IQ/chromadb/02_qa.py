'''
INTERVIEW QUESTIONS – CHROMADB PERSISTENCE

1. What is the purpose of persist_directory in Chroma?
   - It enables storing embeddings and documents on disk.
   - Allows reloading the vector database without recomputing embeddings.

2. What happens if persist_directory is not provided?
   - Chroma runs in-memory.
   - All stored vectors are lost when the program stops.

3. Why is persistence important in production systems?
   - Avoids re-embedding large datasets.
   - Saves computation time and cost.

4. How does persistence improve performance?
   - Prevents repeated PDF processing and embedding generation.
   - Speeds up application startup time.

5. What exactly gets saved in the persistence directory?
   - Embedding vectors.
   - Original document chunks.
   - Metadata and indexing structures.

6. Does persistence mean Chroma becomes a server?
   - No.
   - It still runs locally unless explicitly deployed as a service.

7. Can we reload a persisted Chroma database?
   - Yes.
   - By initializing Chroma with the same persist_directory and embedding model.

8. Why must the same embedding model be used when reloading?
   - Because stored vectors were generated using that embedding space.
   - Changing models breaks similarity consistency.

9. How does persistence reduce infrastructure cost?
   - Prevents repeated embedding computation.
   - Reduces CPU/GPU usage.

10. What is a real-world scenario where persistence is mandatory?
   - Large document repositories.
   - Enterprise knowledge bases.
   - Production chatbots serving repeated queries.
'''
