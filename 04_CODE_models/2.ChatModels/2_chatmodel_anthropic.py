from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# Load environment variables (ANTHROPIC_API_KEY must be set)
load_dotenv()

# Initialize model
model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022"
)

# Invoke model
result = model.invoke("What is the capital of India?")

# Print only the answer
print(result.content)

# Optional: Check type
# print(type(result))