"""
Document Loaders in LangChain

Document loaders are components in LangChain used to load data from
different sources and convert it into a standardized format
(usually as Document objects). These documents can then be used for
chunking, embedding, retrieval, and generation in AI pipelines.

Example structure of a Document object:

Document(
    page_content="The actual text content",
    metadata={"source": "filename.pdf", ...}
)
"""