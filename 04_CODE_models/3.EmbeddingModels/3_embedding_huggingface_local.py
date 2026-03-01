from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Define query
query = "Delhi is the capital of India"

# Generate embedding vector
query_vector = embedding.embed_query(query)

print(query_vector)
print("Vector length:", len(query_vector))