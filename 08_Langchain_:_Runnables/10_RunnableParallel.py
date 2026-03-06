from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

# model
model = ChatOllama(model='llama3.2:1b')

# parser
parser = StrOutputParser()

# prompts
prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

# parallel chain
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

# visualize chain
print("\nChain Graph")
print("-" * 40)
parallel_chain.get_graph().print_ascii()

# result
result = parallel_chain.invoke({'topic': 'AI'})

print(result)


# Output (Dictionary)
{
    "tweet": "Imagine a future where machines can learn, adapt and assist us with ease. "
             "That's the promise of Artificial Intelligence. From healthcare to transportation, "
             "AI is revolutionizing various industries and transforming our lives in incredible ways "
             "#ArtificialIntelligence #AI #FutureOfWork",

    "linkedin": """
Here's a potential LinkedIn post about AI:

**Unlocking the Power of Artificial Intelligence**

The future of work is here, and it's changing the game for businesses across industries.
Artificial intelligence (AI) is no longer just a buzzword — it's a reality that's transforming
the way we work, interact with each other, and solve complex problems.

From automating repetitive tasks to creating personalized customer experiences,
AI is opening up new opportunities for innovation and growth.

But what does this mean for you? Here are a few key takeaways:

• Increased efficiency  
  AI can automate processes, freeing up time for more strategic work and focus on high-priority initiatives.

• Improved accuracy  
  AI-powered tools can analyze vast amounts of data, reducing errors and improving decision-making.

• Enhanced customer experience  
  Personalization is no longer just about marketing — it's a key differentiator in the market.

Whether you're a business leader, developer, or simply looking to stay ahead of the curve,
AI is an exciting area to explore.

What are your thoughts on AI? Are you seeing any benefits from implementing AI solutions
in your organization?

Let's connect and discuss how we can harness the power of AI to drive innovation and growth.

#ArtificialIntelligence #AI #Innovation #Growth #Leadership #Business #Development
"""
}