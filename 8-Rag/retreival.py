from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

persist_directory="db/chroma_db"

embedding_model=OllamaEmbeddings(model="nomic-embed-text:latest")


db=Chroma(persist_directory=persist_directory, embedding_function=embedding_model)

query="Who is Sundar Pichai?"

retriever=db.as_retriever(search_kwargs={"k":3})
results=retriever.invoke(query)

print("Search results:")
for i, res in enumerate(results):
    print(f"\nResult {i+1}")
    print("Source:", res.metadata["source"])
    print("Content:")
    print(res.page_content)

    