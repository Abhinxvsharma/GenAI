import streamlit as st

from langchain_ollama import ChatOllama

from langchain_core.prompts import ChatPromptTemplate,PromptTemplate


llm=ChatOllama(model="phi3:mini", temperature=0.9,max_output_tokens=100,max_input_tokens=1000,max_tokens=250)


st.title("Ollama Bot")
st.write("Ask me anything! Type 'exit' or 'quit' to end the conversation.")


user = st.text_input("Enter your message here:")

# writing the templates using f string

template2=f'''
You are a helpful Cyber Security assistant. Answer the questions in a concise manner.
Always answer the question according to the user's context the way he/she wants.
'''
#writing the templates using triple quotes

template = '''
 You are a helpful Cyber Security assistant. Answer the questions in a concise manner.
Always answer the question according to the user's context the way he/she wants.
If user asks for a term out of cyber security, answer that sorry i am not trained to answer that question. Always answer in a concise manner.

User: {user_input}

'''


#using prommpt template

template=PromptTemplate(input_variables=["user_input"], template='''
You are a helpful Cyber Security assistant. Answer the questions in a concise manner.
Always answer the question according to the user's context the way he/she wants.
If user asks for a term out of cyber security, answer that sorry i am not trained to answer that question. Always answer in a concise manner.

User: {user_input}

''')

if st.button("Hanji Dasso"):
    if user.lower() in ["exit", "quit"]:
        st.write("Goodbye! Have a great day!")
    else:
        # output = llm.invoke(ChatPromptTemplate.from_template(template).format(user_input=user)) #yeh f string and triple quotes ke liye hai
        prompt=template.invoke({"user_input": user})  #yeh prompt template ke liye hai
        output = llm.invoke(prompt)
        st.write(f"Bot: {output.content}")    

