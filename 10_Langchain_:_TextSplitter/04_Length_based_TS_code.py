from langchain_text_splitters import CharacterTextSplitter

# text
text = """
Artificial Intelligence is transforming many industries.
It helps machines learn from data and make intelligent decisions.
AI is used in healthcare, finance, education, and robotics.
"""

# Length-based splitter
splitter = CharacterTextSplitter(
    chunk_size=50,     # max characters per chunk
    chunk_overlap=10   # overlap between chunks
)

# Split text
chunks = splitter.split_text(text)

# Display chunks
for i, chunk in enumerate(chunks, 1):
    print(f"\nChunk {i}")
    print("-" * 20)
    print(chunk)