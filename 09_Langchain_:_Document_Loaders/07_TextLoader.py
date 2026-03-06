from langchain_community.document_loaders import TextLoader

loader = TextLoader('09_Langchain_:_Document_Loaders/cricket_poem.txt', encoding='utf-8')

docs = loader.load()

print("\nDOCS")
print('-'*40)
print(docs)

print("\nTYPE (DOCS)")
print('-'*40)
print(type(docs))

print("\nDOCS[0]")
print('-'*40)
print(docs[0])

print("\nTYPE (docs[0])")
print('-'*40)
print(type(docs[0]))

# Extracting Only Page Content:
print("\nPAGE CONTENT") # YOU CAN EXTRACT METADATA as well but not required as much
print('-'*40)
print(docs[0].page_content)

'''
Length of Doc : 1
Access Doc : docs[0]
Type of docs[0] : Document Type
Actual content : docs[0].page_content
'''


# DOCS
# ----------------------------------------
# [Document(metadata={'source': '09_Langchain_:_Document_Loaders/cricket_poem.txt'}, page_content='On the green field under a blazing sun, A cricket match has just begun.\nThe bowler runs with focused might, The batter stands prepared to fight.\n\nThe crowd erupts with every cheer, As leather ball cuts through the air.\nA perfect swing, the bat connects, The ball flies past the boundary\nspecs.\n\nFielders chase with desperate speed, Every run a rising need. The\nscoreboard ticks with silent pride, As hope and tension walk beside.\n\nA yorker strikes, the stumps take flight, The stadium roars in sheer\ndelight. Yet courage stands at every crease, Where pressure never seems\nto cease.\n\nFrom dusty streets to grandest ground, Cricket’s magic can be found. In\nevery heart the passion lives, For joy this timeless game still gives.\n')]

# TYPE (DOCS)
# ----------------------------------------
# <class 'list'>

# DOCS[0]
# ----------------------------------------
# page_content='On the green field under a blazing sun, A cricket match has just begun.
# The bowler runs with focused might, The batter stands prepared to fight.

# The crowd erupts with every cheer, As leather ball cuts through the air.
# A perfect swing, the bat connects, The ball flies past the boundary
# specs.

# Fielders chase with desperate speed, Every run a rising need. The
# scoreboard ticks with silent pride, As hope and tension walk beside.

# A yorker strikes, the stumps take flight, The stadium roars in sheer
# delight. Yet courage stands at every crease, Where pressure never seems
# to cease.

# From dusty streets to grandest ground, Cricket’s magic can be found. In
# every heart the passion lives, For joy this timeless game still gives.
# ' metadata={'source': '09_Langchain_:_Document_Loaders/cricket_poem.txt'}

# TYPE (docs[0])
# ----------------------------------------
# <class 'langchain_core.documents.base.Document'>

# PAGE CONTENT
# ----------------------------------------
# On the green field under a blazing sun, A cricket match has just begun.
# The bowler runs with focused might, The batter stands prepared to fight.

# The crowd erupts with every cheer, As leather ball cuts through the air.
# A perfect swing, the bat connects, The ball flies past the boundary
# specs.

# Fielders chase with desperate speed, Every run a rising need. The
# scoreboard ticks with silent pride, As hope and tension walk beside.

# A yorker strikes, the stumps take flight, The stadium roars in sheer
# delight. Yet courage stands at every crease, Where pressure never seems
# to cease.

# From dusty streets to grandest ground, Cricket’s magic can be found. In
# every heart the passion lives, For joy this timeless game still gives.