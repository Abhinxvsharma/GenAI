# from langchain_ollama import ChatOllama



# llm = ChatOllama(model="phi3:mini")

# output=llm.invoke("What is the capital of India ?")

# print(output.content)


# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv


# load_dotenv()

# llm =ChatOpenAI(model="gpt-5")

# output=llm.invoke("Give me five latest india news in bullet points")

# print(output.content)


from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
import os
from dotenv import load_dotenv


load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3.5-9B:together",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)

model=ChatHuggingFace(llm=llm)

output=model.invoke("What is the capital of India ?")
print(output.content)