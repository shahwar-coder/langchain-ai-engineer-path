'''
Q1. What does “agentic” capability mean in LangChain?
A.
Agentic capability means the LLM can decide what action to take,
select appropriate tools, execute them, and use the results
to generate a final answer.
It is no longer just responding — it is acting.
'''

# Example:
# User: "Weather in Mumbai and convert to Fahrenheit"
# Agent:
#   → Call weather API
#   → Use calculator tool
#   → Return combined result


'''
Q2. What is an AI Agent in technical terms?
A.
An AI Agent is an LLM-driven system that follows a
Thought → Action → Observation loop,
allowing it to choose and execute tools dynamically
to accomplish a goal.
'''

# Example Flow:
# Think: "Need weather data"
# Act: Call weather_tool()
# Observe: "28°C"
# Think: "Convert to Fahrenheit"
# Act: calculator_tool()
# Final answer returned


'''
Q3. Why can’t a raw LLM perform agentic tasks alone?
A.
A raw LLM only predicts text.
It cannot execute code, call APIs, access databases,
or manage multi-step decision loops.
Agent frameworks provide the execution layer.
'''

# Example:
# Raw LLM can SAY "Calling API..."
# But it cannot actually execute the API request.


'''
Q4. How does LangChain technically enable agent behavior?
A.
LangChain provides:
1. Tool abstractions (Python functions as tools)
2. Agent types (ReAct, tool-calling, structured agents)
3. Execution loop management
It orchestrates tool calls and feeds results back to the LLM.
'''

# Example:
# Define:
# def calculator_tool(x): return x * 2
# LangChain agent decides when to use it automatically.


'''
Q5. Why is agentic capability valuable in production systems?
A.
Real-world tasks are multi-step and require external interactions.
Agentic systems enable workflow automation, API orchestration,
and decision-based execution beyond simple Q&A.
'''

# Example:
# Task: "Book a flight"
# Steps:
#   → Search flights
#   → Check availability
#   → Make payment
#   → Send confirmation


'''
Q6. What are the trade-offs of agentic systems?
A.
Agents introduce higher latency, higher cost,
greater complexity, and debugging challenges.
They are powerful but require careful control and monitoring.
'''

# Example:
# Single LLM call → fast
# Agent loop with 3 tool calls → slower & more expensive


'''
Q7. What additional benefit does LangChain provide beyond agent loops?
A.
LangChain supports structured output control,
schema validation, and JSON parsing,
making LLM responses backend-compatible and API-ready.
'''

# Example:
# Instead of:
# "The answer is 42"
# Force output:
# {"result": 42}
# Parsed into Pydantic model safely.
