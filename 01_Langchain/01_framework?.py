'''
Q1. What is a framework in simple words?
A.
A framework is a pre-built structure that helps you build applications
faster by providing rules, tools, and reusable components.
It saves you from writing everything from scratch.
'''
# Example:
# Instead of writing raw HTTP handling,
# FastAPI lets you just define:
# @app.get("/")
# def home(): return {"msg": "Hi"}


'''
Q2. How is a framework different from a library?
A.
In a library, YOU call the code.
In a framework, the framework calls YOUR code.
This is called Inversion of Control.
'''
# Example:
# Library:
# math.sqrt(16)
#
# Framework:
# @app.get("/")
# def route(): ...
# FastAPI decides when to call route()


'''
Q3. What does it mean that a framework is "opinionated"?
A.
It means the framework enforces certain design patterns,
folder structures, and best practices.
You follow its rules to build applications.
'''
# Example:
# Django expects:
# models.py
# views.py
# urls.py
# You follow its structure.


'''
Q4. What are the main benefits of using a framework?
A.
- Faster development
- Structured architecture
- Built-in best practices
- Reusable components
- Less boilerplate code
'''
# Example:
# FastAPI automatically:
# - validates input
# - generates API docs
# - handles JSON
# No manual implementation needed.


'''
Q5. What does a framework usually provide?
A.
- Routing system
- Request/response handling
- Error handling
- Configuration system
- Built-in utilities
'''
# Example:
# FastAPI provides:
# - Route decorators (@app.get)
# - Validation via Pydantic
# - Swagger documentation


'''
Q6. Give real-world examples of frameworks.
A.
- Django → Python web framework
- FastAPI → API framework
- React → Frontend framework/library
- PyTorch → Deep learning framework
'''
# Example:
# In PyTorch:
# import torch.nn as nn
# You define models using its provided structure.
