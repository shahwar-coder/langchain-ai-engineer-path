'''
TOP 10 INTERVIEW QUESTIONS (RAG + OLLAMA PROJECT)

1. What is RAG and why is it used?
   - Retrieval-Augmented Generation combines document retrieval with LLM generation.
   - It reduces hallucination by grounding answers in real data.

2. Why do we split documents into chunks?
   - LLMs have context limits.
   - Smaller chunks improve retrieval accuracy and semantic matching.

3. What is an embedding?
   - An embedding is a numerical vector representation of text meaning.
   - It allows semantic similarity search using math instead of keywords.

4. Why do we use a vector database like Chroma?
   - To store embeddings and perform fast similarity search.
   - It retrieves relevant chunks based on meaning.

5. What does a retriever do in RAG?
   - Converts user query to embedding.
   - Returns most similar document chunks from vector store.

6. What is the purpose of create_stuff_documents_chain?
   - It injects retrieved chunks into the prompt.
   - It formats context properly before sending to LLM.

7. What does create_retrieval_chain do?
   - It connects retriever and LLM chain.
   - It automates retrieval → formatting → answer generation.

8. Why use session_state in Streamlit?
   - Streamlit reruns script on every interaction.
   - session_state preserves objects like the RAG chain across reruns.

9. Why separate main.py and supporting_functions.py?
   - main.py handles UI.
   - supporting_functions.py handles business logic.
   - This improves maintainability and scalability.

10. Why prefer OllamaLLM over langchain_community.llms.Ollama?
   - OllamaLLM is the official integration package.
   - It ensures better compatibility and future-proof design.
'''
