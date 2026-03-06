'''
🧠 LangChain Model Types — Clear System View

LangChain supports two core model categories:

1️⃣ Language Models (Text → Text)
2️⃣ Embedding Models (Text → Vector)

They solve different but complementary problems.

--------------------------------------------------

1️⃣ Language Models (LLMs / Chat Models)

Input:  Text  
Output: Text  

Used for:
- Question answering
- Summarization
- Translation
- Code generation
- Conversation

Role:
🧠 The reasoning & generation engine

Examples in LangChain:
- ChatOpenAI
- ChatAnthropic
- Ollama (chat models)

--------------------------------------------------

2️⃣ Embedding Models

Input:  Text  
Output: Numeric vector (e.g., 768D)

Used for:
- Semantic search
- RAG retrieval
- Similarity comparison
- Clustering

Role:
📐 Convert meaning into geometry

Examples in LangChain:
- OpenAIEmbeddings
- OllamaEmbeddings
- HuggingFaceEmbeddings

--------------------------------------------------

Why Both Are Needed (RAG Example)

Step 1:
Documents → Embeddings → Vector DB

Step 2:
Query → Embedding → Semantic search

Step 3:
Retrieved context → LLM → Final answer

Embeddings find.
LLMs explain.

--------------------------------------------------

One-Line Summary:

LLMs generate language.
Embeddings encode meaning.
LangChain orchestrates both.
'''