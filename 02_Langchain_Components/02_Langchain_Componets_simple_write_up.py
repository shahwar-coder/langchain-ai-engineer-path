'''
LangChain Components — System-Level Overview

LangChain is built around six core components that
work together to create intelligent LLM applications.

--------------------------------------------------

1️⃣ Models (The Brain)
- Large Language Models like GPT, Claude, Llama, Ollama
- Responsible for understanding and generating text
- Core reasoning engine of the system

Without models → no intelligence.

--------------------------------------------------

2️⃣ Prompts (Instructions)
- Structured inputs given to the model
- Control tone, format, constraints, and behavior
- Example: "Answer only from provided context"

Clear prompts → controlled, reliable output.

--------------------------------------------------

3️⃣ Chains (Workflow Orchestration)
- Connect multiple steps into a pipeline
- Example:
  Question → Retrieve → Generate → Return
- Enables multi-step AI applications

Chains turn single model calls into systems.

--------------------------------------------------

4️⃣ Memory (State Management)
- Stores past interactions
- Maintains conversation context
- Required for chatbots and assistants

Without memory → model forgets previous messages.

--------------------------------------------------

5️⃣ Indexes (Retrieval / RAG Layer)
- Enable semantic document search
- Includes:
  • Text splitting
  • Embeddings
  • Vector databases
  • Similarity search

Indexes allow LLMs to answer from your data.

--------------------------------------------------

6️⃣ Agents (Autonomous Decision Systems)
- Let models choose tools and actions
- Example:
  Use weather API → retrieve data → respond
- Support reasoning + tool usage

Agents move from static Q&A to dynamic AI systems.

--------------------------------------------------

Big Picture Mapping

Models   → Think
Prompts  → Guide thinking
Chains   → Connect steps
Memory   → Remember context
Indexes  → Search knowledge
Agents   → Act intelligently

--------------------------------------------------

Final Insight:

If the LLM is the brain,
LangChain is the orchestration layer that manages
memory, workflows, search, and decision-making
to build complete AI systems.
'''