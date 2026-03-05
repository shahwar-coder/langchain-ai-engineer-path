from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st


st.set_page_config(page_title="Research Tool Application")
st.header("Research Tool")

load_dotenv()

model = ChatOllama(
    model="llama3.2:1b",
    temperature=0.1
    )

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    if not user_input.strip():
        st.warning("Please enter a prompt.")
    else:
        try:
            with st.spinner("Thinking..."):
                result = model.invoke(user_input)
                st.write(result.content)
        except Exception as e:
            st.error(f"Error: {e}")


"""
STREAMLIT + OLLAMA APP (Improved Version) — Concise Summary
============================================================

1️⃣ Page Setup
    st.set_page_config(...)
    st.header(...)
    → Configures UI before anything renders.

2️⃣ Load Environment
    load_dotenv()
    → Loads environment variables (safe practice for keys/config).

3️⃣ Initialize Local LLM
    ChatOllama(
        model="llama3.2:1b",
        temperature=0.1
    )

    - Uses local Ollama model.
    - Low temperature → more deterministic output.
    - Good for summarization tools.

4️⃣ User Input
    st.text_input()
    → Collects prompt from user.

5️⃣ Button Click Logic
    if st.button("Summarize"):

        ✔ Input validation (strip check)
        ✔ Spinner for better UX
        ✔ Try/Except for safe error handling
        ✔ model.invoke() to generate response
        ✔ Display result.content

--------------------------------------------------

Execution Flow:
User Input
    ↓
Validation
    ↓
model.invoke()
    ↓
LLM Response
    ↓
Streamlit Display

--------------------------------------------------

What Improved Here?

✓ Proper page config
✓ Temperature control
✓ Input validation
✓ Loading spinner
✓ Exception handling
✓ Clean UX

--------------------------------------------------

This is a Production-Style Minimal LLM App:
Simple UI + Defensive Coding + Local Model + Clean Control Flow
"""