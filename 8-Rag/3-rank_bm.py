from rank_bm25 import BM25Okapi

corpus = [
    "Hello there good man!",
    "What is the weather today of Ludhiana",
    "The weather of Ludhiana today is very humid"
]

tokenized_corpus = [doc.lower().split(" ") for doc in corpus]

bm25 = BM25Okapi(tokenized_corpus)


query = "weather of Ludhiana"

tokenized_query = query.lower().split(" ")

doc_scores = bm25.get_scores(tokenized_query)
print(doc_scores)