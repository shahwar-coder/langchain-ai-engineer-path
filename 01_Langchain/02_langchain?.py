'''
Q1. What is LangChain in simple words?
A.
LangChain is a framework that helps you build applications
powered by Large Language Models (LLMs).
It connects LLMs with tools, memory, and data sources.
'''
# Example:
# Instead of:
#   user → LLM → answer
#
# You can build:
#   user → retrieve documents → LLM → refined answer


'''
Q2. Why do we need LangChain if we already have GPT?
A.
Raw LLMs can generate text, but they:
- Don’t remember conversations properly
- Can’t access databases by default
- Can’t call tools on their own
LangChain adds structure, memory, and tool integration.
'''
# Example:
# GPT alone cannot query your company database.
# LangChain can:
#   - retrieve data
#   - inject into prompt
#   - generate final answer


'''
Q3. What does “Chain” mean in LangChain?
A.
A Chain means combining multiple steps together
like prompt formatting, LLM calls, tool usage,
and post-processing into one workflow.
'''
# Example:
# Step 1: Format prompt
# Step 2: Call LLM
# Step 3: Parse output
# Step 4: Return structured response


'''
Q4. What core components does LangChain provide?
A.
- Prompt Templates (structured prompts)
- Chains (multi-step workflows)
- Memory (chat history)
- Retrievers (RAG support)
- Agents (tool-using AI systems)
'''
# Example:
# prompt = PromptTemplate(...)
# chain = LLMChain(llm=model, prompt=prompt)


'''
Q5. What is RAG in the context of LangChain?
A.
RAG (Retrieval-Augmented Generation) means:
The LLM answers questions using external documents
retrieved from a vector database.
'''
# Example:
# User asks: "What is our refund policy?"
# System:
#   1. Retrieve policy doc
#   2. Inject into prompt
#   3. LLM generates answer


'''
Q6. What problem does LangChain solve for engineers?
A.
It provides structured abstractions so engineers
don’t manually handle:
- Prompt formatting
- Tool calling logic
- Memory management
- Retrieval pipelines
- Output parsing
'''
# Example:
# Without LangChain:
#   Write custom prompt builders, memory storage,
#   vector search integration manually.
#
# With LangChain:
#   Use built-in components and connect them.
