from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

import os

load_dotenv()

os.getenv("OPENAI_API_KEY", "No API key found")
# with open("file.txt",'w') as f:           // This is just a test to check if the file is created successfully.
#     f.write("hello world")


# llm=ChatOpenAI(model="gpt-5-mini", temperature=0.5)


# while True:
#     query=input("Enter your query:")
#     if query.lower() in ["exit", "quit"]:
#         print("Exiting the program.")
#         break
#     response=llm.invoke(query)
#     print("Response:",response.content)


# llm =ChatOllama(model="phi3:mini",temperature=0.5)
# response=llm.invoke("Who is Elon Musk?")
# print(response.content)


# Embeddings 

# embeddings=OllamaEmbeddings(model="nomic-embed-text:latest")

# text="LangChain is a powerful framework for building applications with language models."
# vector=embeddings.embed_query(text)
# print("Embedding vector:",vector)

# text="LangChain is a powerful framework for building applications with language models."
# embedding=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
# vector=embedding.embed_query(text)

# print("Embedding vector:",vector)




