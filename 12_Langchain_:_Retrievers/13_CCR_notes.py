"""
Contextual Compression Retriever

A Contextual Compression Retriever improves retrieval quality by
removing irrelevant information from retrieved documents and keeping
only the parts that are useful for the user’s query.

Problem with a normal retriever
-------------------------------
Traditional retrievers return entire documents or paragraphs even if
only a small portion of the text is relevant to the query.

Example query

Query:
"What is photosynthesis?"

Retrieved document (traditional retriever):

"The Grand Canyon is a famous natural site.
Photosynthesis is how plants convert light into energy.
Many tourists visit every year."

Problem:
• The retriever returns the entire paragraph
• Only one sentence actually answers the question
• The rest is irrelevant noise
• This wastes the LLM context window


How Contextual Compression Works
--------------------------------

Step 1 — Retrieve documents normally using a retriever.

Step 2 — A compression model (often an LLM or filter) analyzes the
retrieved text and extracts only the relevant parts.

Step 3 — The compressed result is sent to the LLM.


Example result

Compressed output:

"Photosynthesis is how plants convert light into energy."


Why Contextual Compression is Useful
------------------------------------

• Removes irrelevant information
• Saves valuable LLM context space
• Improves answer accuracy
• Reduces noise in retrieved documents


Mental Model
------------

Traditional Retrieval

Query
  ↓
Retriever
  ↓
Full Documents
  ↓
LLM


Contextual Compression Retrieval

Query
  ↓
Retriever
  ↓
Documents
  ↓
Compression Filter
  ↓
Relevant Sentences Only
  ↓
LLM
"""