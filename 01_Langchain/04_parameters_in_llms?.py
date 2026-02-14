'''
Q1. What are parameters in machine learning?
A.
Parameters are the internal numbers that a model learns during training.
They determine how the model transforms input into output.
'''

# Example:
# Linear regression:
# y = wx + b
# w and b are parameters learned from data.


'''
Q2. What are parameters in neural networks?
A.
In neural networks, parameters are mainly weights and biases.
Weights control connection strength between neurons.
Biases shift the output slightly to improve predictions.
'''

# Example:
# output = (w1*x1 + w2*x2) + b
# w1, w2 = weights
# b = bias


'''
Q3. Why are parameters considered the model’s “memory”?
A.
Because parameters store all learned patterns from training data.
They encode grammar, logic, patterns, and relationships.
'''

# Example:
# After training on millions of sentences,
# the learned weights store language structure patterns.


'''
Q4. What does it mean when we say an LLM has billions of parameters?
A.
It means the model contains billions of learned weights and biases.
These numbers collectively store its knowledge and language ability.
'''

# Example:
# GPT-style model:
# billions of floating-point numbers
# stored across transformer layers.


'''
Q5. Do more parameters always mean a better model?
A.
Not necessarily.
More parameters increase capacity, but performance also depends on data quality,
training process, architecture, and alignment techniques.
'''

# Example:
# A poorly trained 100B model
# can perform worse than a well-trained 7B model.


'''
Q6. What is the difference between parameters and hyperparameters?
A.
Parameters are learned during training.
Hyperparameters are set before training and control how learning happens.
'''

# Example:
# Parameters → weights (w1, w2, b)
# Hyperparameters → learning_rate=0.001, batch_size=32
