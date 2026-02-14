'''
Q1. What is Hugging Face?
A.
Hugging Face is an open AI platform for sharing, training,
and deploying machine learning models, especially NLP and LLMs.
It acts like a GitHub for AI models.
'''

# Example:
# You can download a pretrained LLaMA or BERT model
# directly from the Hugging Face Model Hub.


'''
Q2. What is the Hugging Face Model Hub?
A.
The Model Hub is a repository containing thousands of
pretrained models for NLP, vision, audio, and multimodal tasks.
Developers can download, fine-tune, or deploy these models.
'''

# Example:
# Search "mistral" → download model → run locally using transformers.


'''
Q3. What is the Transformers library?
A.
Transformers is Hugging Face’s most popular Python library
that provides APIs to load, tokenize, train, and run
state-of-the-art transformer models easily.
'''

# Example:
# from transformers import pipeline
# generator = pipeline("text-generation", model="gpt2")
# generator("Hello world")


'''
Q4. Why is Hugging Face important in the AI ecosystem?
A.
It removes the need to train models from scratch by
providing ready-to-use pretrained models,
standardized APIs, and open-source collaboration.
'''

# Example:
# Instead of training BERT from zero,
# you load a pretrained BERT model and fine-tune it.


'''
Q5. What else does Hugging Face provide beyond models?
A.
It provides datasets, hosting infrastructure,
inference endpoints, evaluation tools,
and Spaces for deploying demo applications.
'''

# Example:
# Upload a model → deploy via Hugging Face Inference Endpoint.


'''
Q6. How is Hugging Face different from LangChain or OpenAI?
A.
Hugging Face is a model ecosystem and tooling platform.
It is not a single LLM provider (like OpenAI)
and not an orchestration framework (like LangChain).
'''

# Example:
# Hugging Face hosts LLaMA.
# LangChain builds workflows around LLaMA.
# OpenAI provides hosted GPT APIs.
