from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# ─────────────────────────────────────────
# Config
# ─────────────────────────────────────────
persist_directory = "db/chroma_db"

#  Check DB exists before loading
if not os.path.exists(persist_directory) or not os.listdir(persist_directory):
    print(" Vector store not found. Please run ingestion.py first.")
    exit(1)

# Embedding model
embedding_model = OllamaEmbeddings(model="nomic-embed-text:latest")

# Load vector database
db = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model
)

# Retriever
retriever = db.as_retriever(
    search_type="mmr",              #  MMR = diverse results, not just similar
    search_kwargs={"k": 3, "fetch_k": 10}
)

# Prompt Template
template = """
You are an intelligent AI assistant.
Use ONLY the provided context to answer the user's question.

Instructions:
- If the answer is not present in the context, say:
  "I don't know based on the provided context."
- Do not make up information.
- Keep the answer clear, accurate, and concise.
- If multiple documents contain relevant information, combine them properly.

Context:
{context}

Question:
{question}

Helpful Answer:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)

# LLM — lower temperature for factual RAG
llm = ChatOllama(
    model="phi3:mini",
    temperature=0.2      #  0.2 → more accurate answers
)

chain = prompt | llm | StrOutputParser()

# ─────────────────────────────────────────
#  Conversation Loop — keeps running
# ─────────────────────────────────────────
print("\n RAG Assistant Ready! (type 'exit' to quit)\n")

while True:
    user_query = input("You: ").strip()

    if not user_query:
        print("  Please enter a valid question.\n")
        continue

    if user_query.lower() in ["exit", "quit", "q"]:
        print(" Goodbye!")
        break

    # Retrieve relevant chunks
    results = retriever.invoke(user_query)

    if not results:
        print(" No relevant documents found.\n")
        continue

    # Build context
    context = "\n\n".join([
        f"Source: {res.metadata.get('source', 'Unknown')}\n"
        f"Content: {res.page_content}"
        for res in results
    ])

    #  Stream the answer token by token
    print("\n AI Response:\n")
    for chunk in chain.stream({"context": context, "question": user_query}):
        print(chunk, end="", flush=True)

    # ✅ Show sources used
    print("\n\n Sources:")
    seen = set()
    for res in results:
        src = res.metadata.get('source', 'Unknown')
        if src not in seen:
            print(f"  - {src}")
            seen.add(src)
    print()