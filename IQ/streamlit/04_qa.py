'''
1. Why do we use st.session_state in Streamlit applications?

Ans.
Streamlit reruns the entire script on every interaction.
session_state preserves important objects across reruns.


2. What would happen if we did not use session_state for rag_chain?

Ans.
The RAG chain would reset every time the user clicks a button.
Users would lose the processed model state.


3. Why initialize rag_chain to None?

Ans.
It ensures a predictable starting state.
It also allows us to check later whether processing has happened.


4. How does session_state improve user experience?

Ans.
It prevents recomputation and preserves state.
Users can ask multiple questions without rebuilding embeddings.


5. What kind of objects are typically stored in session_state?

Ans.
Long-lived objects like models, vector stores, or chains.
Anything expensive to recompute.


6. Is session_state persistent after app restart?

Ans.
No.
It only persists during the user session, not across server restarts.


7. How does session_state differ from normal variables?

Ans.
Normal variables reset on rerun.
session_state survives reruns within the same session.


8. Why is this pattern important in ML applications?

Ans.
ML pipelines often involve heavy computation.
Persisting results avoids unnecessary recomputation.


9. What architectural concept does session_state support?

Ans.
Stateful interaction in an otherwise stateless execution model.


10. In production, how might state management evolve?

Ans.
It may move to external storage like Redis, databases,
or backend services for distributed systems.
'''
