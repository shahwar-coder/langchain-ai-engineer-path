'''
🧱 Chains in LangChain — Structured Workflow

A Chain is a pipeline where:
Output of one step → automatically becomes input of the next step.

It connects multiple components into a smooth workflow.

--------------------------------------------------

🚨 The Problem Without Chains

In multi-step tasks like:
Summarize → Translate → Format

You must manually:
- Pass variables between steps
- Manage prompt formatting
- Handle errors
- Maintain intermediate outputs

This becomes messy in large systems.

--------------------------------------------------

✅ What Chains Do

Chains automate:
- Data flow between steps
- Execution order
- Input/output handling
- Workflow orchestration

You define the pipeline once,
LangChain manages the execution.

--------------------------------------------------

🔁 Core Concept

Step 1 Output → Step 2 Input → Step 3 Input → Final Result

This creates a structured thinking workflow.

--------------------------------------------------

🏗 Real Use Cases

- RAG pipelines
- Multi-step reasoning
- Extract → Analyze → Generate
- Summarize → Translate → Format
- Tool calling sequences

--------------------------------------------------

🧠 Mental Model

LLM alone = single thinking step  
Chain = organized thinking process  

Modern AI systems are workflows,
not isolated prompts.

--------------------------------------------------

⭐ One-line summary:

Chains connect multiple processing steps into
a clean, automated LLM pipeline.
'''