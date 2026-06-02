from langchain_community.document_loaders import DirectoryLoader,TextLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


import warnings
warnings.filterwarnings(action='ignore',category=DeprecationWarning)


import os
persist_directory="db/chroma_db"
if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)
    
def load_documents(doc_path="docs"):
    if not os.path.exists(doc_path):
        raise FileNotFoundError(f"The directory '{doc_path}' does not exist.")
    
    text_loader = DirectoryLoader(doc_path,
                             glob="**/*.txt",
                             show_progress=True,
                             loader_cls=TextLoader,
                             loader_kwargs={"encoding": "utf-8"})
    
    pdf_loader = DirectoryLoader(doc_path,
                             glob="**/*.pdf",
                             show_progress=True,
                             loader_cls=PyPDFLoader)

    documents=text_loader.load()
    documents.extend(pdf_loader.load())
    if len(documents) == 0:
        raise ValueError(f"No documents found in the directory '{doc_path}'. Please ensure it contains .txt or .pdf files.")
    
    for i , doc in enumerate(documents):
        print(f"Document {i+1}: {doc.metadata['source']},{len(doc.page_content)} characters")
    
    return documents

def chunk_documents(documents,chunk_size=200,chuk_overlap=20):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chuk_overlap)
    
    chunks=text_splitter.split_documents(documents)
    
    if len(chunks) ==0:
        raise ValueError("No chunks were created from the documents. Please check the chunking parameters.")
    
    # for i, chunk in enumerate(chunks):
    #     print(f"Chunk {i+1}: {len(chunk.page_content)} characters, "
    #           f"Source: {chunk.metadata['source']}",
    print(f"Number of chunks: {len(chunks)}")
    print(f"Example chunk content: {chunks[0].page_content[:200]}...")
    return chunks

embedding_model=OllamaEmbeddings(model="nomic-embed-text:latest")
        
def create_vector_store(chunks, persist_directory="db/chroma_db"):
    embedding_model=OllamaEmbeddings(model="nomic-embed-text:latest")
    print("Creating embeddings and storing in Chroma vector store...")
    print("---- Creating Chroma vector store ----")
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"}
    )
    print("--- Finished creating Chroma vector store ---")
    print(f"Vector store created and saved to: {persist_directory}")

    return vector_store
if __name__=="__main__":
    documents=load_documents()
    chunks=chunk_documents(documents)
    create_vector_store(chunks, persist_directory)
    
    vector_store = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)
    
    query = "sundar Pichai?"
    quer_embedding =embedding_model.embed_query(query)
    retreiver = vector_store.as_retriever(search_kwargs={"k": 3})
    result=retreiver.invoke(query)
    print("Search results:")
    for i, res in enumerate(result):
        print(f"Result {i+1}: {res.metadata['source']}, {len(res.page_content)} characters")
    

    


    
