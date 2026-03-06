"""
Load vs Lazy Load in LangChain

1️⃣ load()

load() uses Eager Loading.

• It loads all documents immediately.
• Returns a list of Document objects.
• All files are read and stored in memory at once.

Example mental flow:
Files → load() → [Doc1, Doc2, Doc3, ...]

Best used when:
• The number of files is small.
• Documents are not very large.
• You want all documents available immediately.


2️⃣ lazy_load()

lazy_load() uses Lazy Loading.

• It loads documents only when needed.
• Returns a generator of Document objects.
• Documents are fetched one-by-one instead of all at once.

Example mental flow:
Files → lazy_load() → Doc1 → Doc2 → Doc3 (streamed)

Best used when:
• You are working with large files.
• You have thousands of documents.
• You want to process documents step-by-step (chunking, embedding, indexing).
• You want to reduce memory usage.


Why DirectoryLoader Can Be Slow

DirectoryLoader scans an entire folder and loads many files.

If you use load():

• Every file is opened immediately.
• Every document is loaded into memory.
• If there are hundreds or thousands of files, memory usage increases.
• Processing (chunking + embedding) only starts after everything loads.

So the pipeline waits for all documents before starting work.


How lazy_load() Fixes This

lazy_load() processes files as a stream.

Instead of:

Directory → Load All → Then Process

It becomes:

Directory → Load One File → Process → Load Next File → Process

Benefits:

• Much lower memory usage.
• Faster pipeline start (processing begins immediately).
• Better for large datasets.
• Ideal for production RAG pipelines with many documents.
"""