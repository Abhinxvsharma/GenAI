from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv

import streamlit as st


load_dotenv()
st.set_page_config(page_title="Hugging Face Endpoint Example", page_icon=":robot_face:",layout="wide")
st.title("Hugging Face Endpoint Example")
mo= HuggingFaceEndpoint(repo_id="Qwen/Qwen3.5-9B", task="text-generation", huggingfacehub_api_token=os.getenv("HF_TOKEN"))
st.write("Model loaded successfully!")
st.write(" You can now ask questions to the model. Type your query below:")
st.write("Example: What is the capital of India?")




llm= ChatHuggingFace(llm=mo, temperature=0.5)

st.write("## Enter your query:")
query = st.text_input("Your Query", "")
if query:
    response = llm.invoke(query)
    st.write("## Response:")
    st.write(response.content)

# print(response.content)




