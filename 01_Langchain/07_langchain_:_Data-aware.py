'''
Q1. What does “data-aware” mean in the context of LangChain?
A.
Data-aware means the LLM can access and use external, proprietary,
or real-time data before generating a response.
Instead of guessing, it retrieves relevant information and grounds
its answer in actual documents.
'''

# Example:
# User: "What is our refund policy?"
# System:
#   → Retrieve company document chunk
#   → Inject into prompt
#   → LLM answers using real policy


'''
Q2. Why are raw LLMs not sufficient for enterprise use?
A.
Raw LLMs are trained on public data with a knowledge cutoff.
They do not know proprietary company data and may hallucinate.
Enterprises require grounded, accurate, and explainable outputs.
'''

# Example:
# Asking about internal HR policy
# Without RAG → hallucinated generic answer
# With RAG → retrieved internal HR document → accurate answer


'''
Q3. What are the main technical steps in a RAG pipeline?
A.
1. Load documents
2. Split text into chunks
3. Convert text into embeddings
4. Store vectors in a vector database
5. Retrieve relevant chunks
6. Inject retrieved context into the prompt
'''

# Example:
# PDF → chunk → embedding → store in Pinecone
# Query → embedding → similarity search → inject context


'''
Q4. Why is RAG preferred over fine-tuning in many production systems?
A.
RAG allows real-time updates without retraining.
Fine-tuning is expensive, static, and harder to maintain.
RAG is cheaper, scalable, and easier to evolve.
'''

# Example:
# New policy added
# Fine-tuning → retrain model
# RAG → just update vector database


'''
Q5. Why choose LangChain instead of building RAG manually?
A.
LangChain provides modular abstractions like document loaders,
text splitters, retrievers, and chains.
It reduces boilerplate and enables provider-agnostic architecture.
'''

# Example:
# Swap FAISS → Pinecone
# Swap OpenAI → Anthropic
# Without rewriting full pipeline


'''
Q6. What architectural transformation does data-awareness enable?
A.
It transforms an LLM from a probabilistic text generator
into a grounded reasoning system connected to real data.
'''

# Example:
# Raw LLM → predicts most likely text
# Data-aware LLM → retrieves verified context before answering
