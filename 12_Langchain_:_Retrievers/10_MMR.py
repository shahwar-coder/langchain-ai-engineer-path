# imports
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


# sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]


# embedding model
embedding_model = OllamaEmbeddings(model="nomic-embed-text")


# create FAISS vector store
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)


# enable MMR retrieval
retriever = vectorstore.as_retriever(
    search_type="mmr",                     # enable MMR
    search_kwargs={
        "k": 3,                            # number of results
        "lambda_mult": 1                   # relevance-diversity balance # 0 is extreme diversity
    }
)


# query
query = "What is langchain?"

results = retriever.invoke(query)


# print results
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)


# --- Result 1 ---
# LangChain is used to build LLM based applications.

# --- Result 2 ---
# Chroma is used to store and search document embeddings.

# --- Result 3 ---
# LangChain makes it easy to work with LLMs.