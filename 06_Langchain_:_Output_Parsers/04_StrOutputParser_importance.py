'''
Why StrOutputParser is Important (LangChain)

When an LLM is called directly using model.invoke(),
the response returned is a message object
(e.g., AIMessage) that contains metadata and the text content.

To use the generated text in the next step of a pipeline,
we often need the raw string instead of the full message object.

--------------------------------------------------

Problem Without StrOutputParser

In multi-step workflows (chains), the output of one step
must become the input of the next step.

However, LLM outputs are objects like:

AIMessage(content="...")

If this object is passed directly into another prompt template,
the template may not receive the clean text it expects.

--------------------------------------------------

Solution: StrOutputParser

StrOutputParser extracts only the textual content from the
LLM response and converts it into a plain string.

Flow with parser:

Prompt → LLM → StrOutputParser → Clean Text → Next Prompt → LLM

This ensures that the next component in the chain receives
properly formatted text.

--------------------------------------------------

Why It Matters

StrOutputParser enables:

- Clean data flow between chain components
- Automatic extraction of text from LLM responses
- Simpler multi-step pipelines
- Reliable chaining of prompts and models

Without a parser, developers would need to manually access
response.content at each step.

--------------------------------------------------

Summary

StrOutputParser converts the LLM's response object into
plain text, making it easy to pass outputs between steps
in a LangChain pipeline.
'''