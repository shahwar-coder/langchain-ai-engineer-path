"""
Why Do We Use a Retriever When Vector Stores Already Support Similarity Search?

Vector stores can directly perform similarity search like this:

    results = vectorstore.similarity_search(query, k=2)

However, in LangChain we often convert the vector store into a retriever:

    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    results = retriever.invoke(query)

The reason is flexibility.

A retriever provides an abstraction layer that allows us to implement
custom retrieval strategies instead of relying on simple similarity search.

This means we can modify how documents are retrieved without changing
the rest of the pipeline (RAG chain, agents, etc.).

Retrievers also follow the Runnable interface in LangChain, so they
can easily integrate with chains, pipelines, and other components.
"""