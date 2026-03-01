from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st


st.set_page_config(page_title="Research Tool Application")
st.header("Research Tool")

load_dotenv()

model = ChatOllama(
    model="llama3.2:1b",
    temperature=0.1
    )

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
- Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""
)

prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
}
)

if st.button("Summarize"):
    try:
        with st.spinner("Generating explanation..."):
            result = model.invoke(prompt)
            st.subheader("📖 Explanation")
            st.write(result.content)
    except Exception as e:
        st.error(f"Error: {e}")
        

"""
STREAMLIT + PROMPT TEMPLATE + OLLAMA
=====================================

What This Version Adds:
-----------------------
This is now a *structured prompt-driven research explainer app*.

1️⃣ UI Controls
    - Paper selection (selectbox)
    - Explanation style selection
    - Length selection

    → Instead of free-text prompt,
      user configures structured parameters.

2️⃣ PromptTemplate
    - Uses LangChain PromptTemplate
    - Injects:
        {paper_input}
        {style_input}
        {length_input}
    - Enforces:
        ✓ Mathematical details
        ✓ Code snippets
        ✓ Analogies
        ✓ No guessing rule

    This is controlled prompt engineering.

3️⃣ Prompt Compilation
    template.invoke({...})
    → Produces final formatted prompt
    → Sent to model

4️⃣ Model Execution
    model.invoke(prompt)
    → LLM generates explanation
    → Displayed in Streamlit

--------------------------------------------------

Execution Flow:
User Selections
    ↓
PromptTemplate Formatting
    ↓
LLM Invocation
    ↓
Structured Explanation Output

--------------------------------------------------

Engineering Improvements Here:

✓ Structured prompt (not raw user input)
✓ Deterministic behavior (temperature=0.1)
✓ Clear instruction boundaries
✓ Defensive instruction: "Insufficient information available"
✓ Cleaner UI segmentation
✓ Spinner + error handling

--------------------------------------------------

Conceptually:

You moved from:
    Simple text → LLM

To:
    Configurable structured reasoning system

This is closer to:
    - Internal research assistants
    - Paper explainer tools
    - Controlled AI UX systems

--------------------------------------------------

Core Takeaway:

PromptTemplate + UI controls
= Controlled generation pipeline
= Safer + More predictable outputs
"""