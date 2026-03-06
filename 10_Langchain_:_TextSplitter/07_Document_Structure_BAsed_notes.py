"""
Document Structure–Based Text Splitting

Document Structure–Based splitting divides text according to the
natural structure of the document instead of fixed chunk sizes.

It uses elements like:
• headings
• sections
• paragraphs
• code blocks
• class or function definitions

For example:
- In Markdown → split by headings (#, ##, ###)
- In code → split by class or function definitions
- In documents → split by sections or paragraphs

Benefits

• Preserves logical structure of the document.
• Keeps related information together.
• Improves embedding quality and retrieval accuracy.
• Very useful for structured content like documentation,
  codebases, research papers, and markdown files.

Example idea

Markdown document
    ↓
Split by headings
    ↓
Section-based chunks

Python code
    ↓
Split by class / function definitions
    ↓
Meaningful code chunks
"""