'''
🧠 LangChain Memory — Concise Explanation

Problem:
LLM API calls are stateless.
Each request is independent and does not remember past conversation.
Without manually sending history, the model loses context.

Example:
Q1: Who is Narendra Modi?
Q2: How old is he?
Without memory → “he” has no reference.

--------------------------------------------------

Solution:
LangChain Memory stores past messages
and automatically injects them into future prompts.

It turns:
Stateless calls → Context-aware conversations.

--------------------------------------------------

Types of Memory

1️⃣ ConversationBufferMemory
- Stores full conversation history.
- Best for short chats.
- May grow large in long conversations.

2️⃣ ConversationBufferWindowMemory
- Stores only last N exchanges.
- Controls token usage.
- Good for medium-length chats.

3️⃣ Summary Memory
- Summarizes older messages.
- Keeps context compact.
- Ideal for long conversations.

4️⃣ Custom Memory
- Stores structured key information.
- Example: user name, preferences.
- Used in advanced personalized systems.

--------------------------------------------------

Core Insight:

LLMs don’t remember.
Memory is the software layer that adds remembering ability.

--------------------------------------------------

One-Line Summary:

LangChain Memory transforms stateless LLM APIs into context-aware conversational systems.
'''