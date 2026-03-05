'''
Structured Output (LLM Concept)

Structured output means forcing an LLM to return results
in a predefined format (usually JSON or a schema) instead
of free-form text.

--------------------------------------------------

Problem:
LLMs normally generate human-readable paragraphs.

Example:
"Morning: Visit Eiffel Tower, Afternoon: Louvre..."

This is hard for programs to reliably parse.

--------------------------------------------------

Solution:
Return structured data like JSON.

Example:
[
  {"time": "Morning", "activity": "Visit Eiffel Tower"},
  {"time": "Afternoon", "activity": "Visit Louvre"}
]

Now the program can easily access fields such as:
item["time"], item["activity"].

--------------------------------------------------

Why It Matters:
Structured output makes LLM responses machine-friendly
and programmable.

It enables:
- automation
- APIs
- dashboards
- agents
- workflow systems

--------------------------------------------------

LangChain Role:
LangChain helps enforce structured responses using:
- JSON output parsing
- Pydantic schemas
- structured output chains

--------------------------------------------------

Summary:
Structured output converts LLM responses from
unstructured text into predictable data that
software systems can reliably use.
'''