'''
Problem Highlight — Static Prompting in the Research Tool

In the current code, the app directly sends user_input
to the model using:

    model.invoke(user_input)

This means the model receives only raw text,
without any structured system instruction.

--------------------------------------------------

What’s the Problem?

1️⃣ No System Guidance
- No defined role (e.g., "You are a research assistant")
- No constraint enforcement
- No format control

2️⃣ Output Depends Entirely on User Wording
- If user writes clearly → good output
- If user writes vaguely → inconsistent output

3️⃣ No Structure or Control
- Cannot enforce:
  • "5 lines exactly"
  • Bullet format
  • Academic tone
  • Concise summary

4️⃣ Inconsistent Behavior
Different prompts produce different styles,
lengths, and reasoning depth.

--------------------------------------------------

Why This Happens

Because the application uses static prompting:
User text → Model → Output

There is no:
- Prompt template
- Role-based instruction
- Controlled formatting

--------------------------------------------------

Engineering Insight

Static prompting = raw string passed to model.
It lacks structure, constraints, and reproducibility.

For production systems,
dynamic structured prompts (with system role
and formatting rules) are preferred.

--------------------------------------------------

One-Line Summary:

The current app relies on static prompting,
which provides no structural control over model behavior,
leading to inconsistent and unpredictable outputs.
'''