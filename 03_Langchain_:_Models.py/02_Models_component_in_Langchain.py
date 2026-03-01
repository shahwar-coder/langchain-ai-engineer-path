'''
🧠 Models Component in LangChain — System View

The Models component is the foundation layer that connects
your application to:

1️⃣ Language Models (LLMs / Chat Models)
2️⃣ Embedding Models

It acts as a universal adapter, hiding provider-specific API differences.

--------------------------------------------------

Model Types

A) Language Models (Text → Text)

• LLMs (Completion Models)
  - Classic text completion
  - Input: prompt
  - Output: generated text
  - Not role-aware by default

• Chat Models
  - Role-based (system, user, assistant)
  - Designed for conversations
  - More structured and context-aware

Used for:
- Q&A
- Summarization
- Translation
- Code generation
- Conversations

--------------------------------------------------

B) Embedding Models (Text → Vector)

• Convert text into numeric vectors
• Capture semantic meaning
• Used for:
  - Semantic search
  - RAG
  - Similarity comparison
  - Clustering

--------------------------------------------------

Why This Component Matters

Without LangChain:
- Every provider has different APIs
- Different request formats
- Different response structures

With LangChain:
- Standard interface (e.g., model.invoke())
- Same response format
- Easy provider switching
- Reduced vendor lock-in

--------------------------------------------------

Architectural Role

Models = Core intelligence layer

Everything else (Chains, RAG, Agents, Memory)
depends on:
- Language models for generation
- Embedding models for retrieval

--------------------------------------------------

One-Line Summary:

The Models component provides a unified interface to
language and embedding models, enabling flexible,
provider-independent AI system design.
'''