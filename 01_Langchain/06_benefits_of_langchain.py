'''
Q0. What are the 3 main benefits of LangChain?
A.
The three main benefits are:
1. Data-aware systems (RAG integration)
2. Agentic behavior (tool usage & decision loops)
3. Structured chains (multi-step workflows)

Together, they convert raw LLMs into production-ready AI systems.
'''

# Example:
# Data-aware → Connect to vector DB
# Agentic → Call APIs / tools
# Chains → Orchestrate multi-step reasoning pipeline
'''
Q1. What does it mean that LangChain makes LLMs “data-aware”?
A.
It means the LLM can access and use external documents or databases
before generating an answer. This is usually done using RAG
(Retrieval Augmented Generation).
'''

# Example:
# User question → retrieve relevant company docs →
# inject into prompt → LLM generates grounded answer


'''
Q2. Why is being data-aware important in production AI systems?
A.
Because LLMs are trained on public data and have a knowledge cutoff.
Without retrieval, they may hallucinate or give outdated answers.
Data-awareness reduces hallucination and improves accuracy.
'''

# Example:
# Asking refund policy without RAG → hallucinated answer
# Asking with RAG → retrieved official policy → accurate answer


'''
Q3. What does “agentic” mean in the context of LangChain?
A.
Agentic means the LLM can decide which tools to use,
execute actions (like APIs or calculations),
and combine results before responding.
'''

# Example:
# User: “Weather in Delhi and 20% tax on 500?”
# Agent:
#   → call weather API
#   → calculate tax
#   → combine outputs
#   → return final answer


'''
Q4. How do Chains improve LLM workflows?
A.
Chains allow multi-step structured pipelines instead of single prompts.
Each step performs a specific task, making the system modular
and easier to maintain.
'''

# Example:
# Step 1 → Summarize document
# Step 2 → Extract key entities
# Step 3 → Generate final report


'''
Q5. Why is a unified interface a major benefit of LangChain?
A.
Different LLM providers have different APIs.
LangChain abstracts these differences so you can switch models
without rewriting business logic.
'''

# Example:
# Swap:
#   OpenAI model → Anthropic model
# Without changing chain structure


'''
Q6. What is the deeper architectural benefit of LangChain?
A.
It transforms an isolated text generator into a system component
by adding memory, tool access, structured workflows,
and integration with external data sources.
'''

# Example:
# Without LangChain:
#   LLM → text prediction only
#
# With LangChain:
#   LLM + retrieval + tools + memory + orchestration
