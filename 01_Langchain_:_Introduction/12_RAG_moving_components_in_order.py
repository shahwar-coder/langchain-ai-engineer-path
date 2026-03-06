'''
End-to-End RAG System — Moving Components View

Think of RAG as independent, swappable building blocks:

--------------------------------------------------

🗂 1️⃣ Storage Layer
- S3 / Cloud bucket / Local storage
- Responsible for storing raw documents

--------------------------------------------------

📥 2️⃣ Document Loader
- Reads PDFs / files
- Extracts clean text

--------------------------------------------------

✂ 3️⃣ Text Splitter
- Breaks large text into chunks
- Controls chunk size & overlap

--------------------------------------------------

🧮 4️⃣ Embedding Model
- Converts text chunks → vectors
- Can be OpenAI / Ollama / Gemini / HF

(Swappable component)

--------------------------------------------------

🗄 5️⃣ Vector Database
- Stores (vector + text + metadata)
- Handles indexing & similarity search
- Chroma / Pinecone / FAISS / Weaviate

(Swappable component)

--------------------------------------------------

🔎 6️⃣ Retriever
- Converts query → embedding
- Searches vector DB
- Returns top-k relevant chunks

--------------------------------------------------

📝 7️⃣ Prompt Builder
- Combines:
  • Retrieved chunks
  • User query
  • System instructions
- Manages token limits

--------------------------------------------------

🤖 8️⃣ LLM (Generation Engine)
- OpenAI / Gemini / Claude / etc.
- Produces final grounded answer

(Swappable component)

--------------------------------------------------

⚙ 9️⃣ Production Layer
- Logging
- Monitoring
- Caching
- Evaluation
- Security

--------------------------------------------------

⭐ Clean Architectural Flow

Documents
  ↓
Loader → Splitter → Embedding Model → Vector DB
                                      ↑
User Query → Query Embedding → Retriever
                                      ↓
Prompt Builder → LLM → Final Answer

--------------------------------------------------

Core Insight:

A RAG system is a set of modular moving components.
Each component can be replaced independently
without redesigning the entire system.
'''