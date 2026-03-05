from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables (GOOGLE_API_KEY must be set)
load_dotenv()

# Initialize Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro"
)

# Invoke model
result = model.invoke("What is the capital of India?")

# Print only the answer
print(result.content)

# Optional: Check type
# print(type(result))