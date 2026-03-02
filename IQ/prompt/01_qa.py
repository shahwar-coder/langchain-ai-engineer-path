'''
1. Why do we explicitly include a <context> section in the prompt?

Ans.
It clearly separates retrieved information from the user question.
This reduces confusion and ensures the LLM treats it as reference material.

Structured prompts improve reliability.


2. Why do we instruct the model to answer “based only on the provided context”?

Ans.
This constrains the model from hallucinating.
It forces grounding in retrieved chunks instead of relying on training memory.


3. What happens if we remove grounding instructions from the prompt?

Ans.
The model may mix its internal knowledge with retrieved context.
This can reduce factual consistency and introduce incorrect details.


4. Why use a template with placeholders like {context} and {input}?

Ans.
Templates standardize the structure of prompts.
They allow dynamic injection of retrieved chunks and user queries.


5. What is the role of clarity in prompt design?

Ans.
LLMs respond better to clear, explicit instructions.
Ambiguous prompts often produce inconsistent outputs.


6. Why avoid overly complex instructions in production prompts?

Ans.
Long prompts increase token usage and latency.
They can also introduce unpredictable behavior.


7. How does prompt structure affect reasoning quality?

Ans.
Structured prompts guide the model’s thought flow.
Clear ordering (context first, question second) improves response coherence.


8. Why might we remove “Think step by step” in production systems?

Ans.
It increases token usage and may expose internal reasoning.
Often concise instructions are more efficient and sufficient.


9. What is the balance between detail and minimalism in prompt design?

Ans.
Enough detail to guide the model,
but not so much that it bloats context or introduces confusion.


10. How would you test whether a prompt is effective?

Ans.
By evaluating answer accuracy, grounding consistency,
and observing hallucination rates across multiple queries.
'''
