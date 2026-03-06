# import retriever
from langchain_community.retrievers import WikipediaRetriever


# initialize retriever
retriever = WikipediaRetriever(top_k_results=2, lang="en")


# define query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"


# fetch documents
docs = retriever.invoke(query)


# print results
for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content[:300])


# --- Result 1 ---
# The India–Pakistan war of 1971, also known as the third Indo-Pakistani war, was a military confrontation between India and Pakistan that occurred during the Bangladesh Liberation War in East Pakistan from 3 December 1971 until the Pakistani capitulation in Dhaka on 16 December 1971.  The war began w

# --- Result 2 ---
# India–Iran relations are the bilateral relationship between the Republic of India and the Islamic Republic of Iran. Independent India and Iran established diplomatic relations on 15 March 1950.
# Contact between both ancient Persia and ancient India date to ancient times, and can be seen through the d