'''
1️⃣ Python List (Linear Scan):

How it works

Query vector
↓
Compare with V1
↓
Compare with V2
↓
Compare with V3
↓
…
↓
Compare with VN
'''
# You must check every vector.
# There is no structure guiding the search.
# It’s a straight line → full scan → O(N).

# [ V1, V2, V3, V4, V5, ... Vn ]
#           ↑
#         scan all


'''
2️⃣ Vector Database (Indexed ANN Search):
How it works

Vectors are organized in a graph or clustered structure.

Query vector
↓
Jump to a close node
↓
Move through nearby connections
↓
Reach nearest neighbors

It does guided navigation, not brute-force comparison.

That’s why search becomes ~O(log N) instead of O(N).
'''

   #    V2 —— V5
   #   /        \
   # V1 —— V3 —— V7
   #          \
   #           V9

# You “walk” the graph instead of scanning everything.

'''BIG INSIGHT'''
# Python list = container only.
# Vector DB = container + intelligent navigation structure.
