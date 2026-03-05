'''
Dynamic Prompt as the Fix for Static Prompting

Earlier Version (Static Prompt):
- Directly passed raw user text to model
- No structure
- No role control
- No format enforcement
- Highly dependent on how user phrased the request
- Inconsistent outputs

Flow:
User Text → LLM → Output

Problem:
Model behavior was unpredictable and loosely controlled.

--------------------------------------------------

Improved Version (Dynamic Prompt with PromptTemplate):

Instead of free-text input,
the app now uses structured UI parameters:
- Paper selection
- Explanation style
- Length requirement

These are injected into a PromptTemplate.

Flow:
User Selections
   ↓
PromptTemplate (structured formatting)
   ↓
LLM Invocation
   ↓
Controlled Output

--------------------------------------------------

What Dynamic Prompt Fixed

1️⃣ Enforced Structure
- Clear formatting rules
- Style & length constraints
- Mathematical + analogy requirements

2️⃣ Reduced Hallucination
- Explicit rule: "Insufficient information available"
- Encourages safer responses

3️⃣ Predictable Output
- Deterministic temperature
- Consistent formatting
- Instruction boundaries defined

4️⃣ Separation of Concerns
- UI handles input
- PromptTemplate handles structure
- Model handles reasoning

--------------------------------------------------

Engineering Insight

Static Prompt:
Prompt = User string

Dynamic Prompt:
Prompt = Parameterized, controlled template

You moved from:
Ad-hoc text generation

To:
Structured, configurable reasoning pipeline

--------------------------------------------------

One-Line Summary:

Dynamic prompting transformed an uncontrolled LLM interface
into a structured, predictable, and production-ready
AI generation system.
'''