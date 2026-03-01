'''
🧠 Language Models in LangChain — Clear Overview

Language Models are AI systems that:
- Understand text
- Generate text
- Process natural language

Input  → Text
Output → Text

Used for:
Q&A, summarization, translation, chatbots, code generation.

--------------------------------------------------

Two Types in LangChain

1️⃣ LLMs (Completion Models)

• Input: Plain text string
• Output: Plain text
• No built-in role awareness
• Traditional text completion style

Example:
Prompt → "Write a story about a robot."
Output → Story continuation

Think:
Smart autocomplete engine.

--------------------------------------------------

2️⃣ Chat Models (Modern Standard)

• Input: Structured messages (system, user, assistant)
• Output: Message object
• Context-aware
• Designed for dialogue

Example:
System → "You are a doctor."
User   → "What is viral fever?"
Assistant → Response

Think:
Conversation-aware AI assistant.

--------------------------------------------------

Key Differences

LLMs        → Text completion  
Chat Models → Role-based conversation  

Today, Chat Models are more commonly used,
especially for RAG, agents, and multi-turn chat systems.

--------------------------------------------------

In LangChain

Both are accessed via a unified interface:
model.invoke(...)

Provider complexity is abstracted away.

--------------------------------------------------

One-Line Summary:

Language Models in LangChain generate text and exist as
traditional completion models (LLMs) and modern
conversation-based chat models.
'''