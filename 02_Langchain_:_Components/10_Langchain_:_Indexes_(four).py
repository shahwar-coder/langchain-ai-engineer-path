'''
📚 Indexes in LangChain — Concise System View

Indexes connect your LLM application to external knowledge
(PDFs, websites, databases, private documents).

Without indexes:
LLM only uses its training data.

With indexes:
LLM can answer from your data.
This enables RAG (Retrieval-Augmented Generation).

--------------------------------------------------

Core Index Components

1️⃣ Document Loader
- Imports external data into the system.

2️⃣ Text Splitter
- Breaks large documents into smaller chunks
- Handles token limits and improves retrieval quality.

3️⃣ Vector Store
- Converts chunks → embeddings
- Stores vectors for semantic search
- Examples: Chroma, Pinecone, FAISS

4️⃣ Retriever
- Converts user query → embedding
- Finds top-k similar chunks from vector store

--------------------------------------------------

How It Works

Data → Load → Split → Embed → Store
User Query → Embed → Retrieve → LLM → Answer

--------------------------------------------------

⭐ Final Insight

Indexes make your LLM searchable over your own knowledge,
enabling grounded, accurate, context-aware responses.
'''