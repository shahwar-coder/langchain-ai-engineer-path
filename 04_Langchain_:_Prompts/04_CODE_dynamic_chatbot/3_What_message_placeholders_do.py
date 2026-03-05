"""
MESSAGESPLACEHOLDER — CLEAR & ORGANIZED EXPLANATION
===================================================

PROBLEM WE ARE TRYING TO SOLVE
------------------------------
Chat models do NOT remember previous conversation automatically.

Every time we call the model, we must send:
    1) System message (behavior rules)
    2) Entire chat history
    3) New user question

If we forget chat history → the model forgets context.


------------------------------------------------------------
WHAT IS MessagesPlaceholder?
------------------------------------------------------------

MessagesPlaceholder(variable_name="chat_history")

It is a dynamic insertion slot inside a ChatPromptTemplate.

It tells LangChain:

    "At this position in the template,
     insert the full list of previous messages."


------------------------------------------------------------
HOW THE TEMPLATE IS STRUCTURED
------------------------------------------------------------

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("chat_history"),
    ("human", "{question}")
])

This means the final prompt will be built in this order:

    1️⃣ System message
    2️⃣ Insert chat_history here
    3️⃣ Add new human question


------------------------------------------------------------
WHAT chat_history CONTAINS
------------------------------------------------------------

chat_history = [
    HumanMessage("What is cricket?"),
    AIMessage("Cricket is a bat and ball sport.")
]

This represents previous conversation.


------------------------------------------------------------
WHAT format_messages() DOES
------------------------------------------------------------

formatted_prompt = chat_template.format_messages(
    chat_history=chat_history,
    question="Explain DRS simply."
)

LangChain builds this final message list:

    System: You are a helpful assistant.
    Human: What is cricket?
    AI: Cricket is a bat and ball sport.
    Human: Explain DRS simply.

Now the model sees full context.


------------------------------------------------------------
WHY MessagesPlaceholder IS IMPORTANT
------------------------------------------------------------

Without it:
    - You must manually combine system + history + question.
    - Easy to make mistakes.
    - Hard to scale.

With it:
    - Template structure is clean.
    - History insertion is automatic.
    - Code becomes modular and production-ready.


------------------------------------------------------------
IMPORTANT CLARIFICATION
------------------------------------------------------------

MessagesPlaceholder does NOT store memory.

It only:
    Inserts whatever list you pass as chat_history.

You are still responsible for maintaining chat_history.


------------------------------------------------------------
MENTAL MODEL (SIMPLE)
------------------------------------------------------------

Think of it like a document template:

    Header
    [Paste previous conversation here]
    New question

MessagesPlaceholder is that "paste here" section.


------------------------------------------------------------
CORE TAKEAWAY
------------------------------------------------------------

MessagesPlaceholder solves the context problem
by allowing previous conversation messages
to be dynamically injected into a structured prompt template.

It enables:
    ✓ Multi-turn conversations
    ✓ Clean chat architecture
    ✓ Scalable memory handling
    ✓ Production-style chat systems
"""