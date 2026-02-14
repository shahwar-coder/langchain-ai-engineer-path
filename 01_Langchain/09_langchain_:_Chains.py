'''
Q1. What is a Chain in LangChain?
A.
A Chain is a structured sequence of components
where the output of one step becomes the input of the next.
It enables multi-step LLM workflows instead of single prompt calls.
'''

# Example:
# User → Prompt Template → LLM → Output Parser → Final Response


'''
Q2. Why are Chains important in real-world AI systems?
A.
Real-world tasks require multiple steps such as retrieval,
summarization, extraction, and formatting.
Chains allow these steps to be connected into a clean pipeline.
'''

# Example:
# 1. Retrieve documents
# 2. Summarize content
# 3. Extract key points
# 4. Generate report


'''
Q3. What problem do Chains solve compared to manual orchestration?
A.
Without chains, developers manually pass outputs between
multiple LLM calls, handle formatting, manage state,
and deal with errors.
Chains provide structured orchestration and cleaner architecture.
'''

# Example:
# Manual:
# result1 = llm(prompt1)
# result2 = llm(f"Summarize {result1}")
# With Chain:
# define step1 → step2 → connected automatically


'''
Q4. What are common types of Chains?
A.
Common conceptual types include:
- Sequential chains (step-by-step flow)
- Parallel chains (multiple branches)
- Router chains (conditional routing)
- Retrieval chains (RAG pipelines)
'''

# Example:
# Router chain:
# If question is math → use math_chain
# If question is legal → use legal_chain


'''
Q5. Why do enterprises prefer Chains in production?
A.
Chains provide modularity, maintainability,
observability, and reusability.
Each step can be tested and modified independently.
'''

# Example:
# Update retrieval logic without touching summarization logic.


'''
Q6. What is the key difference between Chains and Agents?
A.
Chains follow deterministic orchestration —
predefined structured workflows.
Agents follow dynamic decision-making —
LLM chooses actions autonomously.
'''

# Example:
# Chain:
# Always Step1 → Step2 → Step3
# Agent:
# Decide whether to use Tool A or Tool B based on context
