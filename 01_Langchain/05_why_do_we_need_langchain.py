'''
Q1. Why do we need LangChain if LLMs are already powerful?
A.
LLMs are powerful text generators but they are stateless and isolated.
They cannot access real-time data, tools, or structured workflows by default.
LangChain connects LLMs to memory, tools, and external data sources.
'''

# Example:
# Without LangChain:
#   user → LLM → answer
#
# With LangChain:
#   user → retrieve docs → LLM → refined answer


'''
Q2. How does LangChain solve the “outdated knowledge” problem?
A.
LLMs have a training cutoff and no real-time access.
LangChain enables Retrieval Augmented Generation (RAG),
allowing the model to fetch fresh documents before answering.
'''

# Example:
# Step 1: Embed documents
# Step 2: Store in vector database
# Step 3: Retrieve relevant chunks
# Step 4: Inject into prompt
# Step 5: LLM generates grounded answer


'''
Q3. Why are raw LLM APIs insufficient for production systems?
A.
Raw LLM APIs only generate text.
Production systems require memory, multi-step reasoning,
tool usage, structured outputs, logging, and error handling.
LangChain provides abstractions for these needs.
'''

# Example:
# Production app requires:
# - conversation memory
# - database access
# - API calls
# - structured JSON output


'''
Q4. How does LangChain simplify working with multiple LLM providers?
A.
Different providers have different APIs and formats.
LangChain provides a unified abstraction layer,
making it easier to switch between OpenAI, Anthropic, or local models.
'''

# Example:
# Swap:
#   OpenAI() → Anthropic()
# Minimal change in higher-level chain logic.


'''
Q5. How does LangChain make LLMs domain-aware?
A.
LLMs do not know private company data.
LangChain enables document loading, chunking, embedding,
vector storage, and retrieval so the model can answer using proprietary data.
'''

# Example:
# Load PDF → split → embed → store in vector DB
# Query → retrieve relevant chunks → pass to LLM


'''
Q6. What is the deeper architectural role of LangChain?
A.
LLM is the brain.
LangChain acts as the system layer that connects the brain
to tools, memory, data sources, and workflows,
making it possible to build production-grade AI systems.
'''

# Example:
# Brain only:
#   LLM → probability engine
#
# With system:
#   LLM + tools + memory + retrieval + orchestration
