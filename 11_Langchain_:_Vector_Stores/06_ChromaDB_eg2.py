from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document


# -------------------------
# Create documents
# -------------------------

doc1 = Document(
    page_content="""
Virat Kohli is one of the most successful and consistent batsmen in IPL history.
Known for his aggressive batting style and exceptional consistency,
he has been a key player for Royal Challengers Bangalore.
""",
    metadata={"team": "Royal Challengers Bangalore"}
)

doc2 = Document(
    page_content="""
Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to multiple titles.
He is known for his elegant batting style and calm leadership.
""",
    metadata={"team": "Mumbai Indians"}
)

doc3 = Document(
    page_content="""
MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to several IPL titles.
He is renowned for his finishing abilities and calm decision-making.
""",
    metadata={"team": "Chennai Super Kings"}
)

doc4 = Document(
    page_content="""
Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket.
He plays for Mumbai Indians and is known for his deadly yorkers.
""",
    metadata={"team": "Mumbai Indians"}
)

doc5 = Document(
    page_content="""
Ravindra Jadeja is a dynamic all-rounder for Chennai Super Kings.
He contributes with bat, ball, and exceptional fielding.
""",
    metadata={"team": "Chennai Super Kings"}
)

docs = [doc1, doc2, doc3, doc4, doc5]


# -------------------------
# Embeddings model
# -------------------------

embeddings = OllamaEmbeddings(model="nomic-embed-text")


# -------------------------
# Vector store
# -------------------------

vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_db",
    collection_name="sample"
)


# -------------------------
# Add documents
# -------------------------

vector_store.add_documents(docs)


# -------------------------
# Similarity search
# -------------------------

print("\nSIMILARITY SEARCH")
print("-" * 40)

results = vector_store.similarity_search(
    query="Who among these are bowlers?",
    k=2
)

for r in results:
    print(r.page_content.strip())
    print("Metadata:", r.metadata)
    print()


# -------------------------
# Similarity with score
# -------------------------

print("\nSIMILARITY SEARCH WITH SCORE")
print("-" * 40)

results_score = vector_store.similarity_search_with_score(
    query="Who among these are bowlers?",
    k=2
)

for doc, score in results_score:
    print(doc.page_content.strip())
    print("Metadata:", doc.metadata)
    print("Score:", score)
    print()


# -------------------------
# Metadata filtering
# -------------------------

print("\nMETADATA FILTER (Chennai Super Kings)")
print("-" * 40)

filtered = vector_store.similarity_search(
    query="",
    filter={"team": "Chennai Super Kings"}
)

for r in filtered:
    print(r.page_content.strip())
    print("Metadata:", r.metadata)
    print()