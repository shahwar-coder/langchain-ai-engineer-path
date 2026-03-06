from langchain_community.document_loaders import PyPDFLoader

# Load the PDF
loader = PyPDFLoader('09_Langchain_:_Document_Loaders/cricket_20_points.pdf')

# Read documents
docs = loader.load()

# Display raw documents
print("\nDOCS")
print("-" * 40)
print(docs)

# Display type of returned object
print("\nTYPE")
print("-" * 40)
print(type(docs))

# Display number of pages (length)
print("\nTOTAL PAGES")
print("-" * 40)
print(len(docs))

# Display actual content of first page
print("\nCONTENT (PAGE 1)")
print("-" * 40)
print(docs[0].page_content)

# Display metadata
print("\nMETADATA (PAGE 1)")
print("-" * 40)
print(docs[0].metadata)

# DOCS
# ----------------------------------------

# [
#     Document(
#         metadata={
#             "producer": "ReportLab PDF Library - (opensource)",
#             "creator": "(unspecified)",
#             "creationdate": "2026-03-05T22:57:38+00:00",
#             "author": "(anonymous)",
#             "keywords": "",
#             "moddate": "2026-03-05T22:57:38+00:00",
#             "subject": "(unspecified)",
#             "title": "(anonymous)",
#             "trapped": "/False",
#             "source": "09_Langchain_:_Document_Loaders/cricket_20_points.pdf",
#             "total_pages": 1,
#             "page": 0,
#             "page_label": "1"
#         },
#         page_content="""
# Cricket – 20 Key Points

# Cricket is a popular bat-and-ball sport played between two teams of eleven players.

# The game originated in England and later spread to many countries around the world.

# The main objective is to score more runs than the opposing team.

# A cricket field is usually oval-shaped with a rectangular pitch in the center.

# Each team has batsmen, bowlers, and fielders.

# The batsman tries to score runs by hitting the ball with a bat.

# The bowler delivers the ball toward the batsman to dismiss them.

# Fielders try to stop the ball and prevent the batsmen from scoring runs.

# Runs can be scored by running between the wickets or hitting boundaries.

# If the ball reaches the boundary after touching the ground, it is worth four runs.

# If the ball crosses the boundary without touching the ground, it is worth six runs.

# There are different formats of cricket such as Test, One Day International (ODI), and T20.

# Test cricket is the longest format and can last up to five days.

# ODI matches consist of 50 overs per team.

# T20 cricket is a shorter and more fast-paced format with 20 overs per team.

# Cricket is especially popular in countries like India, Australia, England, and Pakistan.

# Major tournaments include the ICC Cricket World Cup and the T20 World Cup.

# The player who scores the most runs in a match is often considered the top batsman.

# The bowler who takes the most wickets is considered the best bowler in the match.

# Cricket is known for its spirit of sportsmanship and teamwork.
# """
#     )
# ]


# TYPE
# ----------------------------------------
# <class 'list'>


# TOTAL PAGES
# ----------------------------------------
# 1


# CONTENT (PAGE 1)
# ----------------------------------------

# Cricket – 20 Key Points

# Cricket is a popular bat-and-ball sport played between two teams of eleven players.

# The game originated in England and later spread to many countries around the world.

# The main objective is to score more runs than the opposing team.

# A cricket field is usually oval-shaped with a rectangular pitch in the center.

# Each team has batsmen, bowlers, and fielders.

# The batsman tries to score runs by hitting the ball with a bat.

# The bowler delivers the ball toward the batsman to dismiss them.

# Fielders try to stop the ball and prevent the batsmen from scoring runs.

# Runs can be scored by running between the wickets or hitting boundaries.

# If the ball reaches the boundary after touching the ground, it is worth four runs.

# If the ball crosses the boundary without touching the ground, it is worth six runs.

# There are different formats of cricket such as Test, One Day International (ODI), and T20.

# Test cricket is the longest format and can last up to five days.

# ODI matches consist of 50 overs per team.

# T20 cricket is a shorter and more fast-paced format with 20 overs per team.

# Cricket is especially popular in countries like India, Australia, England, and Pakistan.

# Major tournaments include the ICC Cricket World Cup and the T20 World Cup.

# The player who scores the most runs in a match is often considered the top batsman.

# The bowler who takes the most wickets is considered the best bowler in the match.

# Cricket is known for its spirit of sportsmanship and teamwork.



# METADATA (PAGE 1)
# ----------------------------------------

# {
#     "producer": "ReportLab PDF Library - (opensource)",
#     "creator": "(unspecified)",
#     "creationdate": "2026-03-05T22:57:38+00:00",
#     "author": "(anonymous)",
#     "keywords": "",
#     "moddate": "2026-03-05T22:57:38+00:00",
#     "subject": "(unspecified)",
#     "title": "(anonymous)",
#     "trapped": "/False",
#     "source": "09_Langchain_:_Document_Loaders/cricket_20_points.pdf",
#     "total_pages": 1,
#     "page": 0,
#     "page_label": "1"
# }