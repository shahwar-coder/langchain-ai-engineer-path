from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings

# Text with different topics
text = """
Farmers grow crops like wheat and rice. Agriculture supports food production.
The IPL is a popular cricket league in India. Many international players participate.
Terrorism is a global security concern. Governments work together to prevent attacks.
"""

# Embedding model (used to understand meaning)
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Semantic splitter
splitter = SemanticChunker(embeddings)

# Perform semantic splitting
chunks = splitter.split_text(text)

# Display results
print(len(chunks))
print(chunks)