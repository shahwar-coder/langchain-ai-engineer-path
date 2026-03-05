from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(model="llama3.2:1b")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() == 'exit':
        break
    result = model.invoke(user_input)
    print("AI: ", result.content)

# You: Hello
# AI:  Hello. Is there something I can help you with or would you like to chat?
# You: What is the difference between cheese and cottage cheese?
# AI:  Cheese and cottage cheese are both dairy products, but they have some key differences in terms of their production process, texture, taste, and nutritional content.

# Here are the main differences:

# 1. **Production Process:** Cheese is made by adding enzymes to milk, which break down the lactose into simpler sugars that can be absorbed by the body. The curds (solid parts) are then separated from the whey (liquid parts). Cottage cheese, on the other hand, is made by curdling milk with acid, such as vinegar or lemon juice, and then straining out the whey.
# 2. **Texture:** Cheese has a more solid and crumbly texture due to its higher moisture content and the presence of casein, a protein that binds the cheese together. Cottage cheese has a soft and creamy texture due to its high water content and the presence of casein as well, but also the addition of lactic acid, which breaks down some of the proteins.
# 3. **Taste:** Cheese tends to have a richer, more complex flavor profile than cottage cheese, with notes of buttery, nutty, or fruity flavors depending on the type of cheese. Cottage cheese has a milder, slightly tangy taste due to its lower lactose content and higher water content.
# 4. **Nutritional Content:** Both cheeses and cottage cheese are good sources of protein, calcium, and vitamins. However, cheese tends to be higher in fat and calories due to its higher moisture content. Cottage cheese is often fortified with additional nutrients like vitamin D, calcium, and probiotics, which may not be present in as much of the regular cottage cheese.
# 5. **Calcium Content:** Cheese generally has more calcium than cottage cheese, especially if it's a hard or aged variety.

# In summary, while both cheeses and cottage cheese are nutritious dairy products, they have distinct differences in terms of their production process, texture, taste, and nutritional content.
# You: exit

'''
BIG PROBLEM:
-> This does not have context.
-> Conversation History is key
'''