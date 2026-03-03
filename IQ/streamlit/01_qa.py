'''
1. Why do we separate UI logic (main.py) from business logic (supporting_functions.py)?

Ans.
Separating UI and backend logic keeps the system clean and maintainable.
It allows you to modify the interface without touching core RAG functionality.


2. Why import backend functions instead of writing everything in one file?

Ans.
Modularity improves readability and scalability.
It also makes testing and debugging easier since logic is isolated.


3. Why is the os module required in a Streamlit RAG app?

Ans.
Streamlit provides a file object, not a file path.
We use os to create directories and save the uploaded file locally.


4. What architectural principle does this import structure reflect?

Ans.
Separation of concerns.
Each layer has a clear responsibility — UI handles interaction, backend handles computation.


5. What would happen if UI and RAG logic were tightly coupled?

Ans.
The code would become harder to maintain.
Even small UI changes could affect retrieval and embedding logic.


6. Why is Streamlit used instead of a traditional backend framework?

Ans.
Streamlit is fast to prototype and ideal for interactive ML applications.
It reduces boilerplate for UI creation.


7. How does importing only specific functions improve clarity?

Ans.
It makes dependencies explicit.
Other developers immediately see what backend capabilities the UI uses.


8. Why is this import structure helpful for scaling the system later?

Ans.
It allows replacing Streamlit with another frontend
without changing the core RAG pipeline.


9. In production, how might this structure evolve?

Ans.
UI, retrieval service, and LLM service could be deployed as separate microservices.


10. What does this import design indicate about overall system architecture?

Ans.
It indicates a layered design:
Presentation layer (UI) calling application logic (RAG engine).
'''
