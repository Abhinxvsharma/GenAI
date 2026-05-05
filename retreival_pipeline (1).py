from langchain_chroma import Chroma
#from langchain_openai import OpenAIEmbeddings

from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv()

persistence_directory = "db/chroma_db"

#Load embeddings and vector store
#embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

embedding_model=OllamaEmbeddings(model='nomic-embed-text:latest')

db= Chroma(
    persist_directory=persistence_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space": "cosine"}
)

#Search for relevant documents
query = "Which island does Spacex lease for its launches in the Pacific ??"

retreiver= db.as_retriever(search_kwargs={"k":3})

retreiver= db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 5,
        "score_threshold": 0.3
    }
)

relevant_docs= retreiver.invoke(query)

print(f"User Query: {query}\n")
#Display results

print("--- Context ---")
for i,doc in enumerate(relevant_docs,1):
    print(f"\nDocument {i}:\n{doc.page_content}\n")

