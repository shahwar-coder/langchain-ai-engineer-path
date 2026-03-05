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

chain = template_report | model | parser | template_summary | model | parser

result = chain.invoke({'topic': 'Black Hole'})

print(result)

# Here is a 5-line summary of the text:

# A black hole is a region in space where gravity is so strong that nothing can escape, formed when a massive star collapses and warps spacetime around it.

# There are four types of black holes, each with unique properties and formation mechanisms, ranging from stellar to intermediate-mass and supermassive.

# Black holes have several distinct properties, including event horizons, singularities, ergospheres, and Hawking radiation, which influence space and time.

# Scientists infer the presence of black holes by observing effects such as X-ray binaries, stellar motions, radio emissions, and gravitational waves.

# Further research is needed to fully understand black holes and their mysterious nature.