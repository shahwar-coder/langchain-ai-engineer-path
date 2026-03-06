"""
RAG (Retrieval-Augmented Generation) – High Level Flow

RAG combines external knowledge retrieval with an LLM to generate
more accurate and grounded responses.

Pipeline Overview
-----------------

Query + Retrieved Context
        ↓
       Prompt
        ↓
        LLM
        ↓
     Response


Key Stages of RAG
-----------------

1. Indexing
   Documents are collected, split into chunks, converted into embeddings,
   and stored in a vector database.

   Documents → Chunking → Embeddings → Vector Store


2. Retrieval
   When a user query arrives, it is converted into an embedding and used
   to search the vector database for the most relevant documents.

   Query → Embedding → Similarity Search → Relevant Documents


3. Augmentation
   The retrieved documents are added as context to the prompt sent to the LLM.

   Query + Retrieved Context → Prompt


4. Generation
   The LLM generates the final answer using both the user query and the
   retrieved context.

   Prompt → LLM → Response


Mental Model
------------

Knowledge Base
      ↓
Vector Search
      ↓
Context
      ↓
LLM Reasoning
      ↓
Answer
"""