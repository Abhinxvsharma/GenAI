from langchain_ollama import ChatOllama
from langchain_classic.memory import ConversationBufferMemory,ConversationSummaryMemory,ConversationTokenBufferMemory
from langchain_classic.chains import ConversationChain

# LLM
llm = ChatOllama(model="phi3:mini",temperature=0.5)

# while True:
#     user=input("Enter your query :")
#     if user.lower()=='exit':
#         break
#     response=llm.invoke(user)
#     print(response.content)

# Memory
# memory = ConversationBufferMemory()
# memory=ConversationSummaryMemory(llm=llm)
memory=ConversationTokenBufferMemory(llm=llm,max_tokens=5)

# Conversation Chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)


while True:
    user=input("Enter your query :")
    if user.lower()=='exit':
        break

    elif user.lower()=='history':
        print(memory.buffer)
    response=conversation.predict(input=user)
    print(response)
# Chat
# print(conversation.predict(input="Hi"))
# print(conversation.predict(input="My name is John"))
# print(conversation.predict(input="What is my name?"))