'''
Q1. What is an LLM in simple words?
A.
An LLM (Large Language Model) is a powerful text prediction system.
It reads massive amounts of text during training and learns to predict the next token based on probability.
'''

# Example:
# Input:
#   "The capital of France is"
# Output:
#   "Paris"


'''
Q2. What does an LLM actually learn?
A.
An LLM learns statistical patterns between tokens.
It does not “understand” meaning like humans; it learns which token is most likely to come next.
'''

# Example:
# P("Paris" | "The capital of France is") → High probability
# P("Banana" | "The capital of France is") → Very low probability


'''
Q3. What is a token in LLM terminology?
A.
A token is a small unit of text processed by the model.
It can be a word, part of a word, punctuation, or symbol.
'''

# Example:
# "Artificial Intelligence"
# Might become:
# ["Artificial", "Intelligence"]


'''
Q4. Why are modern LLMs built using Transformers?
A.
Transformers use the attention mechanism.
Attention helps the model focus on relevant words in a sentence to understand context.
'''

# Example:
# Sentence:
#   "The cat that chased the mouse was tired."
# Attention links:
#   "was tired" → "cat"


'''
Q5. Why are LLMs called “Large”?
A.
They contain billions or trillions of parameters.
More parameters allow the model to capture complex and subtle language patterns.
'''

# Example:
# Small model → limited reasoning ability
# Large model → better pattern recognition and fluency


'''
Q6. What are the limitations of a raw LLM?
A.
A raw LLM has no persistent memory, no direct database access,
no real-time awareness, and cannot use tools on its own.
It only predicts text based on input and training data.
'''

# Example:
# GPT alone cannot:
#   - Query your company database
#   - Fetch live stock prices
#   - Access private documents
