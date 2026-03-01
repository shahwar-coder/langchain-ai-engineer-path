"""
RESEARCH TOOL — COMPLETE FLOW (Structured & Concise)
=====================================================

PROJECT STRUCTURE
-----------------
07_CODE_prompt/
│
├── prompt_generator.py   → Creates & saves PromptTemplate (template.json)
├── template.json         → Serialized prompt configuration
├── research_UI.py        → Streamlit app (main runtime)
└── output.png            → Example output (optional)

------------------------------------------------------------

STEP 1️⃣  PROMPT CREATION (prompt_generator.py)
------------------------------------------------
- Define PromptTemplate
    • input_variables:
        - paper_input
        - style_input
        - length_input
    • validate_template=True
    • Structured instructions:
        - Mathematical details
        - Code snippets
        - Analogies
        - No guessing rule

- Save template:
    template.save("template.json")

KEY IDEA:
Prompt is now a configuration asset, not hardcoded text.


------------------------------------------------------------

STEP 2️⃣  TEMPLATE SERIALIZATION (template.json)
------------------------------------------------
Contains:
    - input_variables
    - template string
    - template_format = "f-string"
    - validate_template = true
    - _type = "prompt"

WHY IMPORTANT:
    ✓ Portable
    ✓ Version controllable
    ✓ Reloadable
    ✓ Decoupled from UI logic
    ✓ Production-style prompt management


------------------------------------------------------------

STEP 3️⃣  STREAMLIT UI (research_UI.py)
------------------------------------------------

A. App Setup
    - st.set_page_config()
    - st.header()
    - load_dotenv()
    - Initialize ChatOllama(model="llama3.2:1b", temperature=0.1)

B. User Controls
    - Paper selection (selectbox)
    - Style selection
    - Length selection

C. Load Prompt From Disk
    template = load_prompt("template.json")

IMPORTANT:
Prompt logic is NOT in this file anymore.


------------------------------------------------------------

STEP 4️⃣  CHAIN CONSTRUCTION (LCEL PIPELINE)
------------------------------------------------

When button clicked:

    chain = template | model

This means:
    PromptTemplate → LLM

This is LangChain Expression Language (LCEL).

Flow:
    Dict Inputs
        ↓
    Template Formatting
        ↓
    Model Invocation
        ↓
    AIMessage Output


------------------------------------------------------------

STEP 5️⃣  EXECUTION
------------------------------------------------

result = chain.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

st.write(result.content)

Output:
Structured explanation aligned with:
    - Style
    - Length
    - Mathematical detail constraint
    - No hallucination instruction


------------------------------------------------------------

FULL SYSTEM FLOW (HIGH LEVEL)
------------------------------------------------

User Selection (UI)
        ↓
Dictionary Input
        ↓
Loaded PromptTemplate
        ↓
Formatted Prompt
        ↓
ChatOllama (Local LLM)
        ↓
Structured Explanation
        ↓
Streamlit Display


------------------------------------------------------------

ARCHITECTURAL IMPROVEMENTS YOU ACHIEVED
------------------------------------------------

✓ Prompt separated from UI logic
✓ Prompt stored as reusable JSON config
✓ Deterministic generation (low temperature)
✓ Clean LCEL pipeline (template | model)
✓ Modular structure
✓ Production-style organization
✓ Easy future upgrade:
      - Add output parser
      - Add RAG
      - Add caching
      - Add logging


------------------------------------------------------------

CORE ENGINEERING TAKEAWAY
------------------------------------------------------------

You moved from:

    UI → Hardcoded Prompt → Model

To:

    UI → Configurable Prompt Asset → Model

That is a clean separation of:
    - Interface
    - Prompt Logic
    - Model Layer

This is how scalable LLM systems are structured.
"""