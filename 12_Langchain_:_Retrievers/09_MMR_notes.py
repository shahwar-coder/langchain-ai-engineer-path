"""
Maximal Marginal Relevance (MMR)

MMR is a retrieval strategy used to return documents that are both
relevant to the query and diverse from each other.

Problem with normal similarity search
-------------------------------------
Similarity search only focuses on relevance. As a result, many retrieved
documents can be very similar and repeat the same information.

Example documents

D1: "Climate change is causing glaciers to melt rapidly in the Arctic region."
D2: "Glaciers in the Arctic are melting at an alarming rate due to rising temperatures."
D3: "Deforestation in the Amazon is accelerating global climate change."
D4: "Climate change is increasing the frequency of wildfires in California."
D5: "Rising sea levels due to climate change threaten coastal cities like Mumbai and New York."


Similarity Search Result
------------------------
Query: "Climate change impacts"

Top 3 results:

1. D1 → Arctic glaciers melting
2. D2 → Arctic glaciers melting
3. D3 → Deforestation in Amazon

Problem:
D1 and D2 are almost the same topic → redundant information.


MMR Retrieval Result
--------------------
Query: "Climate change impacts"

Top 3 results:

1. D1 → Arctic glaciers melting
2. D4 → Wildfires in California
3. D5 → Rising sea levels in coastal cities

What changed?
MMR keeps the most relevant document first,
then selects the next documents that are relevant but also different
from already selected ones.


Why MMR is useful in RAG
------------------------
• Reduces duplicate context
• Increases information diversity
• Provides broader coverage of a topic
• Makes better use of the LLM context window


Mental model
------------
Similarity search → "Most similar documents"

MMR → "Relevant but different documents"
"""