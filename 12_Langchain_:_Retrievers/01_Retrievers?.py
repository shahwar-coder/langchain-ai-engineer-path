"""
What are Retrievers?

A retriever is a component in LangChain that retrieves the most
relevant documents from a data source in response to a user's query.

Instead of generating answers itself, the retriever's job is to
search the knowledge base and return useful document chunks
that can help answer the question.

Key Points

• Retrievers search for documents relevant to the query.
• They work with different data sources such as vector databases,
  APIs, files, or other storage systems.
• Multiple types of retrievers exist depending on the retrieval strategy.
• In LangChain, retrievers follow the Runnable interface, so they
  can easily be used inside pipelines and chains.
"""