from langchain_core.prompts import PromptTemplate

# template
template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True,
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
- Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""
)

template.save('07_CODE_prompt/template.json')

# ====== END ========
# ====== END ========
# ====== END ========
# ====== END ========
# ====== END ========
# ====== END ========

# template.json (content)
'''
{
    "name": null,
    "input_variables": [
        "length_input",
        "paper_input",
        "style_input"
    ],
    "optional_variables": [],
    "output_parser": null,
    "partial_variables": {},
    "metadata": null,
    "tags": null,
    "template": "\nPlease summarize the research paper titled \"{paper_input}\" with the following specifications:\n\nExplanation Style: {style_input}\nExplanation Length: {length_input}\n\n1. Mathematical Details:\n- Include relevant mathematical equations if present in the paper.\n- Explain the mathematical concepts using simple, intuitive code snippets where applicable.\n\n2. Analogies:\n- Use relatable analogies to simplify complex ideas.\n\nIf certain information is not available in the paper, respond with: \"Insufficient information available\" instead of guessing.\n\nEnsure the summary is clear, accurate, and aligned with the provided style and length.\n",
    "template_format": "f-string",
    "validate_template": true,
    "_type": "prompt"
}
'''


# ====


"""
PROMPT TEMPLATE SAVE — WHAT JUST HAPPENED
=========================================

You did:
    template.save("template.json")

LangChain serialized your PromptTemplate
into a JSON configuration file.

--------------------------------------------------

1️⃣ What Got Saved?

The JSON contains:

- input_variables
- template string
- template_format ("f-string")
- validation flag
- metadata fields
- _type = "prompt"

This means your prompt is now:
    ✔ Portable
    ✔ Version-controllable
    ✔ Re-loadable
    ✔ Production-ready

--------------------------------------------------

2️⃣ Why This Is Important (Backend Perspective)

You just separated:

    Prompt Logic
    FROM
    Application Code

That means:

- Prompt can evolve independently
- Prompt can be reviewed like code
- Prompt can be versioned in Git
- Prompt can be reused across services
- Prompt can be loaded dynamically

This is enterprise-grade prompt management.

--------------------------------------------------

3️⃣ How To Load It Back

from langchain_core.prompts import load_prompt

loaded_template = load_prompt("07_CODE_prompt/template.json")

prompt = loaded_template.invoke({
    "paper_input": "Attention Is All You Need",
    "style_input": "Technical",
    "length_input": "Medium"
})

--------------------------------------------------

4️⃣ What validate_template=True Did

It ensured:

- All variables in the template string
  match input_variables.
- No missing placeholders.
- No extra unused variables.

It prevents runtime prompt errors.

--------------------------------------------------

5️⃣ Conceptual Upgrade You Just Made

You moved from:

    Hardcoded prompt string

To:

    Prompt as configuration artifact

This is how serious AI systems are built.

--------------------------------------------------

🔥 Core Insight

Prompts are NOT just strings.
They are configuration assets.
Treat them like API contracts.
"""