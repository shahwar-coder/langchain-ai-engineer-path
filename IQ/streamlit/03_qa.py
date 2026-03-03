'''
1. Why use a sidebar for file upload instead of placing it in the main area?

Ans.
Sidebars help separate configuration inputs from core interaction.
It keeps the UI clean and improves user experience.


2. Why restrict file type to ["pdf"] in file_uploader?

Ans.
It prevents unsupported file formats from entering the pipeline.
This reduces runtime errors and keeps the ingestion logic predictable.


3. Why use a "Process" button instead of automatically processing on upload?

Ans.
Streamlit reruns the script on every interaction.
A button gives controlled execution and prevents unnecessary reprocessing.


4. What does st.file_uploader actually return?

Ans.
It returns an in-memory file-like object.
It is not automatically saved to disk, so we must handle persistence.


5. What problem does separating upload and processing solve?

Ans.
It avoids accidental heavy computation.
Embedding and indexing can be expensive, so explicit triggering is safer.


6. Why is UI structure important in ML applications?

Ans.
Clear input separation reduces user confusion.
It also helps maintain predictable interaction flow.


7. What would happen if we removed the Process button?

Ans.
The app might rebuild embeddings every time the file changes.
This increases latency and resource usage.


8. How does this design support scalability?

Ans.
It allows ingestion to be controlled and potentially moved
to a background task or service later.


9. Why is validation at the UI level useful?

Ans.
It prevents invalid input from reaching backend logic.
Early validation improves system robustness.


10. In a production system, how might this upload mechanism evolve?

Ans.
It could integrate with cloud storage or object stores.
The UI would trigger ingestion jobs asynchronously.
'''
