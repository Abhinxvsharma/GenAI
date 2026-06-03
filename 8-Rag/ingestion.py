from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

import warnings
import os

warnings.filterwarnings(action='ignore', category=DeprecationWarning)

persist_directory = "db/chroma_db"

# Single embedding model instance (no duplicate)
embedding_model = OllamaEmbeddings(model="nomic-embed-text:latest")


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

    documents = text_loader.load()
    documents.extend(pdf_loader.load())

    if len(documents) == 0:
        raise ValueError(f"No documents found in '{doc_path}'.")

    for i, doc in enumerate(documents):
        print(f"Document {i+1}: {doc.metadata['source']}, {len(doc.page_content)} characters")

    return documents


def chunk_documents(documents, chunk_size=800, chunk_overlap=100):  #  fixed typo
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(documents)

    if len(chunks) == 0:
        raise ValueError("No chunks were created. Check chunking parameters.")

    print(f"Number of chunks: {len(chunks)}")
    print(f"Example chunk content: {chunks[0].page_content[:200]}...")
    return chunks


def create_vector_store(chunks, persist_directory="db/chroma_db"):
    #  KEY FIX: Skip if vector store already exists
    if os.path.exists(persist_directory) and os.listdir(persist_directory):
        print(" Vector store already exists! Loading from disk...")
        return Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding_model
        )

    print(" Creating new vector store (only happens once)...")
    os.makedirs(persist_directory, exist_ok=True)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"}
    )

    print(f" Vector store saved to: {persist_directory}")
    return vector_store


if __name__ == "__main__":
    documents = load_documents()
    chunks = chunk_documents(documents)

    #  Will skip embedding if DB already exists
    vector_store = create_vector_store(chunks, persist_directory)

    # Test retrieval
    query = "sundar Pichai?"
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    result = retriever.invoke(query)

    print("\nSearch results:")
    for i, res in enumerate(result):
        print(f"Result {i+1}: {res.metadata['source']}, {len(res.page_content)} characters")