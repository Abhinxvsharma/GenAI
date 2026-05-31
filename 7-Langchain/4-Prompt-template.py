import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Load Model
llm = ChatOllama(model="phi3:mini",temperature=0.9,max_output_tokens=100,max_input_tokens=1000,max_tokens=250)

# Prompt Template
template = PromptTemplate(
    input_variables=["topic", "difficulty"],
    template="""
    You are an expert tutor.

    Explain the topic: {topic}

    Difficulty Level: {difficulty}

    Provide:
    1. Definition
    2. Key Concepts
    3. Real-world Examples
    4. Practice Questions
    """
)

# Streamlit UI
st.title("Chatbot")

topic = st.text_input("Enter Topic")
difficulty = st.selectbox(
    "Select Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("button dabdo"):
    prompt=template.invoke({"topic": topic, "difficulty": difficulty}) 
    output = llm.invoke(prompt)
    st.write(f"Bot: {output.content}")