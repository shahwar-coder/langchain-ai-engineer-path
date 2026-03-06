"""
Wikipedia Retriever

A Wikipedia Retriever is a retriever that queries the Wikipedia API
to fetch relevant information for a given user query.

How It Works

1. You provide a query (for example: "Albert Einstein").
2. The retriever sends this query to the Wikipedia API.
3. Wikipedia returns the most relevant articles related to the query.
4. The retrieved content is returned as LangChain Document objects.
"""