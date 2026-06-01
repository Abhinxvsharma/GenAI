from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

persist_directory="db/chroma_db"

embedding_model=OllamaEmbeddings(model="nomic-embed-text:latest")


db=Chroma(persist_directory=persist_directory, embedding_function=embedding_model)

query="Google"

retriever=db.as_retriever(search_kwargs={"k":3})
results=retriever.invoke(query)

print("Search results:")
for i, res in enumerate(results):
    print(f"Result {i+1}: {res.metadata['source']}, {len(res.page_content)} characters")