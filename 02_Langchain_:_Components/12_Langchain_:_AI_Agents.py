'''
🤖 Agents in LangChain — Clear System View

An AI Agent is:
LLM + Reasoning + Tools + Decision Loop

Unlike a normal chatbot (which only generates text),
an Agent can:
- Decide what to do
- Choose tools
- Execute actions
- Use results to continue reasoning

--------------------------------------------------

How Agents Work

Agent follows a loop:

1️⃣ Think        (Understand the task)
2️⃣ Act          (Select & call a tool)
3️⃣ Observe      (Get tool result)
4️⃣ Repeat       (Reason again if needed)

This is called:
Reason → Act → Observe cycle

--------------------------------------------------

Example 1: Multiply Delhi Temperature by 3

Task requires:
- Fetch live temperature (Weather API)
- Multiply value (Calculator)

Agent flow:
Think → Need temperature
Act → Call weather API
Observe → 25°C
Think → Multiply by 3
Act → Use calculator
Observe → 75
Return final answer

This is reasoning + action.

--------------------------------------------------

Example 2: Plan Trip to Shimla

Agent may:
- Search destinations
- Query hotel API
- Book hotel
- Generate itinerary

Multi-step execution driven by decision making.

--------------------------------------------------

Key Components

LLM          → Reasoning brain
Tools        → External capabilities (APIs, calculator, DB)
Agent Logic  → Chooses which tool to use
Loop         → Continues until task completed

--------------------------------------------------

Comparison

Chatbot → Static text generator  
Agent   → Dynamic problem solver  

--------------------------------------------------

One-Line Summary:

Chains = Fixed workflow  
Agents = Dynamic decision-making systems
'''