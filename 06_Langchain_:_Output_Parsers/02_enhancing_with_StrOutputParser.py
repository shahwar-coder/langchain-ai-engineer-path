from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# model
model = ChatOllama(model='llama3.2:1b')

# prompt template (report)
template_report = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
# prompt template (summary)
template_summary = PromptTemplate(
    template='Write 5 line summary on the following text. \n {text}',
    input_variables=['text']
)

# parser
parser = StrOutputParser()

chain = template_report | model | parser | template_summary | model

result = chain.invoke({'topic': 'Black Hole'})

print(result)

# {
#   "content": "Here is a 5-line summary of the text:\n\nBlack holes are mysterious objects in space that have captivated scientists and astronomers for decades due to their extreme density and gravity. Formed from massive star collapses, black holes have different types including stellar, intermediate-mass, supermassive, and primordial, each with unique properties. Black holes also exhibit characteristics such as the event horizon, singularity, gravitational pull, and Hawking radiation. Observational evidence for black holes includes X-rays, gamma rays, radio waves, star motions, and gravitational lensing. The study of black holes continues to advance, with new discoveries and technological innovations providing insights into their formation and behavior.",
#   "additional_kwargs": {},
#   "response_metadata": {
#     "model": "llama3.2:1b",
#     "created_at": "2026-03-05T08:20:50.762691Z",
#     "done": true,
#     "done_reason": "stop",
#     "total_duration": 5556837791,
#     "load_duration": 139316375,
#     "prompt_eval_count": 1053,
#     "prompt_eval_duration": 1535369999,
#     "eval_count": 137,
#     "eval_duration": 3575308091,
#     "logprobs": null,
#     "model_name": "llama3.2:1b",
#     "model_provider": "ollama"
#   },
#   "id": "lc_run--019cbd15-c011-7620-ba83-cd4dcf55af6e-0",
#   "tool_calls": [],
#   "invalid_tool_calls": [],
#   "usage_metadata": {
#     "input_tokens": 1053,
#     "output_tokens": 137,
#     "total_tokens": 1190
#   }
# }