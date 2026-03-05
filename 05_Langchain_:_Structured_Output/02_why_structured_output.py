'''
Why Structured Output Is Needed (3 Main Use Cases)

Structured output ensures that LLM responses are returned in a
predictable format (like JSON) so software systems can process them
reliably instead of treating them as plain text.

--------------------------------------------------

1️⃣ Data Extraction

LLMs can convert unstructured text into structured fields.

Example:
Resume text → extracted into structured data.

{
  "name": "John Doe",
  "experience_years": 10,
  "role": "Software Engineer",
  "college": "IIT Delhi"
}

This allows the data to be easily stored in databases
and used for search, filtering, or analytics.

Common uses:
- Resume parsing
- Invoice extraction
- Medical records
- Legal documents

--------------------------------------------------

2️⃣ API Building

Applications often require machine-readable responses.

Instead of returning paragraphs, the LLM returns structured data:

{
  "pros": ["Good performance"],
  "cons": ["Poor battery life"],
  "sentiment": 0.5
}

This allows backend services to directly expose the
result through APIs and enables dashboards, analytics,
or frontend applications to consume the data easily.

--------------------------------------------------

3️⃣ Agents (Tool Usage)

Agents need structured instructions to call tools.

Example structured output:

{
  "tool": "calculator",
  "operation": "multiply",
  "numbers": [25, 3]
}

The system can then execute:
calculator(25, 3) → 75

Structured output enables the pipeline:

User Query → LLM reasoning → Structured output → Tool call → Result

--------------------------------------------------

Summary

Structured output converts LLM responses from
unstructured text into machine-readable data,
making them usable in databases, APIs, and agent workflows.
'''