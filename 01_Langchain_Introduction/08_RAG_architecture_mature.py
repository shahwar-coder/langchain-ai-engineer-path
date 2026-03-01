'''
End-to-End RAG Architecture (Concise Explanation)

🔹 Ingestion Phase (Offline)

1. PDF uploaded to storage (e.g., S3)
2. Document loader reads the PDF
3. Text splitter breaks it into pages/chunks
4. Each chunk → embedding vector
5. All embeddings stored in vector database

Result:
Database contains (chunk, embedding) pairs

--------------------------------------------------

🔹 Query Phase (Online)

1. User asks a question
2. Question → converted to embedding (same model)
3. Semantic search compares query vector with stored vectors
4. Top relevant pages retrieved

--------------------------------------------------

🔹 Generation Phase

1. Retrieved pages + User query
   → combined into system prompt
2. Prompt sent to LLM ("Brain")
3. LLM generates context-aware final output

--------------------------------------------------

⭐ Core Flow:

Ingest:
PDF → Split → Embed → Store

Query:
User Question → Embed → Retrieve → Generate

Retrieve first, then generate.
'''