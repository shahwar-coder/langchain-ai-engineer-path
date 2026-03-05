from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

# Initialize embedding model
embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=300
)

# Documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# Query
query = "tell me about bumrah"

# Generate embeddings
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Compute similarity (2D output)
similarities = cosine_similarity([query_embedding], doc_embeddings)

print("Cosine Similarities:")
print(similarities)  
# Example:
# [[0.66305456, 0.34860867, 0.34340637, 0.39610939, 0.3951678]]

# Convert to 1D for easier processing
scores = similarities[0]

# Get best match
best_index = np.argmax(scores)
best_score = scores[best_index]

print("\nQuery:", query)
print("Best Match:", documents[best_index])
print("Similarity Score:", best_score)


'''
EMBEDDING SIMILARITY PIPELINE — SUMMARY
=======================================

1️⃣ What This Code Does
- Converts documents into vector embeddings.
- Converts the query into an embedding.
- Computes cosine similarity between query and documents.
- Finds the most semantically similar document.

--------------------------------------------------

2️⃣ Step-by-Step Flow

(1) Load environment variables
    load_dotenv()

(2) Initialize embedding model
    OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

    - Model generates dense vector representations.
    - dimensions=300 reduces vector size (lower memory, faster compute).

(3) Embed documents
    embed_documents(documents)
    → Returns List[List[float]]

(4) Embed query
    embed_query(query)
    → Returns List[float]

(5) Compute cosine similarity
    cosine_similarity([query_embedding], doc_embeddings)

    - Input must be 2D → hence [query_embedding]
    - Output shape: (1, number_of_documents)

(6) Convert to 1D
    similarities[0]

(7) Select best match
    np.argmax(scores)

--------------------------------------------------

3️⃣ Why Cosine Similarity?
- Measures angle between vectors.
- Ignores magnitude.
- Works well for semantic similarity.
- Range: -1 to 1 (in practice 0 to 1 for embeddings).

Higher score → more semantically similar.

--------------------------------------------------

4️⃣ Why Output is 2D?
sklearn cosine_similarity expects:
    shape (n_samples_X, n_features)
    shape (n_samples_Y, n_features)

Since we compare 1 query vs many documents:
    Output shape → (1, N)

--------------------------------------------------

5️⃣ What This Represents Conceptually

TEXT → VECTOR SPACE → DISTANCE MEASURE → BEST MATCH

This is the core of:
- Semantic Search
- RAG Retrieval
- Vector Databases
- AI Agents

--------------------------------------------------

6️⃣ Backend Engineering Insight

This pattern is the foundation of:
- Document retrieval systems
- Search engines
- Knowledge assistants
- Context selection in LLM apps

Without this layer, LLMs cannot retrieve relevant context.

--------------------------------------------------

🔥 Core Takeaway

Embedding similarity is:
    Meaning-based matching,
    not keyword matching.

This is modern search infrastructure.
'''