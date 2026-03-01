from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Create embedding model
embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)

# Define query
query = "Delhi is the capital of India"

# Generate embedding
query_vector = embedding.embed_query(query)

print(query_vector)
print("Vector length:", len(query_vector))