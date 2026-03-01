from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, load_prompt
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

template = load_prompt("07_CODE_prompt/template.json")


if st.button("Summarize"):
    try:
        chain = template | model
        result = chain.invoke({
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input
        })
        st.write(result.content)
    except Exception as e:
        print(f"Error: {e}")