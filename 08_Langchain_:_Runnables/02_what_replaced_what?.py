# | Old Chain                    | Modern Equivalent                                               |       |                               |
# | ---------------------------- | --------------------------------------------------------------- | ----- | ----------------------------- |
# | LLMChain                     | `PromptTemplate                                                 | LLM   | OutputParser` (LCEL pipeline) |
# | SequentialChain              | `RunnableSequence` using pipe operator `                        | `     |                               |
# | SimpleSequentialChain        | Same as above: `RunnableSequence` (`prompt                      | model | parser`)                      |
# | ConversationalRetrievalChain | `create_history_aware_retriever()` + `create_retrieval_chain()` |       |                               |
# | RetrievalQA                  | `create_retrieval_chain()`                                      |       |                               |
# | RouterChain                  | `RunnableBranch` or `RouterRunnable`                            |       |                               |
# | MultiPromptChain             | `RunnableBranch` with multiple prompts                          |       |                               |
# | HyDEChain                    | `HypotheticalDocumentEmbedder` or custom LCEL pipeline          |       |                               |
# | AgentExecutorChain           | `create_agent()` + `AgentExecutor` or **LangGraph agents**      |       |                               |
# | SQLDatabaseChain             | `create_sql_query_chain()`                                      |       |                               |