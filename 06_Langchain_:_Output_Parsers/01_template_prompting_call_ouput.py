from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

# prompt report
prompt_report = template_report.invoke({'topic': 'black hole'})

result1 = model.invoke(prompt_report)

# prompt summary
prompt_summary = template_summary.invoke({'text': result1.content})

result2 = model.invoke(prompt_summary)

print(result2.content)


# Here is a 5-line summary of the text:

# Black holes are mysterious objects that have captivated human imagination for centuries, with their invisible nature making them impossible to observe directly.
# These regions of spacetime are so dense that not even light can escape, forming when massive stars collapse in on themselves.
# Black holes have several distinct characteristics, including mass, spin, charge, and angular momentum, which define their unique behavior.
# They can form through various processes such as star formation or galaxy mergers, and are inferred by observing effects like gravitational lensing and frame-dragging.
# The study of black holes has far-reaching implications for our understanding of gravity, cosmology, and astrophysics, and continues to be a topic of active research and discovery.