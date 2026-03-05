'''
Why Use PromptTemplate in LangChain?

PromptTemplate turns prompts from raw strings
into reusable, structured, and validated components.

--------------------------------------------------

Problems Without PromptTemplate

- Hardcoded strings
- Repetition of similar prompts
- Difficult maintenance
- Poor scalability
- Risk of formatting mistakes
- No variable checking

Example:
model.invoke("Summarize AI in 5 lines")
model.invoke("Summarize Cricket in 5 lines")

Duplicated structure. Not clean.

--------------------------------------------------

Advantages of PromptTemplate

1️⃣ Reusability
Define once:
"Summarize {topic} in {lines} lines."
Reuse with different inputs.

2️⃣ Clean Variable Injection
Avoid messy string concatenation.
No manual formatting errors.

3️⃣ Validation (Very Important)
PromptTemplate validates:
- Required input variables are provided
- No missing placeholders
- No extra unexpected variables

If a required variable is missing,
it raises an error immediately.

This prevents:
❌ Runtime prompt bugs
❌ Silent formatting failures
❌ Broken production prompts

4️⃣ Scalability
Same template works for:
- APIs
- Multi-user systems
- RAG pipelines
- Agents

5️⃣ Maintainability
Change prompt logic in one place.
All usages update automatically.

6️⃣ Better Structure
Encourages separation of:
- Business logic
- Prompt design
- Model invocation

--------------------------------------------------

Engineering Perspective

Without PromptTemplate:
Prompt = plain, unchecked string

With PromptTemplate:
Prompt = validated, configurable software object

--------------------------------------------------

One-Line Summary:

PromptTemplate enables reusable, validated,
maintainable, and scalable prompt engineering
for production-grade AI systems.
'''