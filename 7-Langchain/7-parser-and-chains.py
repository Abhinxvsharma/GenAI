
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough, RunnableSequence

llm = ChatOllama(model="phi3:mini",temperature=0.5)

# output_parser=CommaSeparatedListOutputParser()
output_parser=StrOutputParser()
# prompt = PromptTemplate(
#     template="""
#     List 5 programming languages.

#     {format_instructions}
#     """,
#     input_variables=[],
#     partial_variables={
#         "format_instructions": output_parser.get_format_instructions()
#     }
# )

# template = """
# You are an intelligent cyber security AI Assistant

# Insruction:
# Answer only related to the cyber security field
# if the question asked is out of the domain of cyber security then answer 
# "sorry i am not trained to answer questions out of my domain "

# Question:
# {question}

# Helpful Answer:
# """
# prompt=PromptTemplate(template=template , input_variables=["question"])


# formatted_prompt=prompt.format(question="What do you mean by Jupyter??")
# # formatted_prompt=prompt.format(**{"question":"What do you mean by Jupyter??"})

# response=llm.invoke(formatted_prompt)


# output_parser=JsonOutputParser()

# prompt=prompt = PromptTemplate(
#     template="""
#     Generate information about a student.
#     {class}
#     {format_instructions}
#     """,
#     input_variables=["class"],
#     partial_variables={
#         "format_instructions": output_parser.get_format_instructions()
#     }
# )

# formatted_prompt=prompt.format(**{"class":"6th"})
# response=llm.invoke(formatted_prompt)



# # Parsing the response

# result=output_parser.parse(response.content)

# print(result)



# in langchain we have majorly 3 types of chains
'''
LLMChain
SimpleSequentialChain
SequentialChain
'''
from langchain_classic.chains import LLMChain
from langchain_classic.chains import SimpleSequentialChain

title_prompt=PromptTemplate(
    input_variables=["topic"],
    template="Generate the catchy title about he blog on the {topic}"
)


# chain=title_prompt | llm | StrOutputParser()
chain= LLMChain(llm=llm,prompt=title_prompt)
result=chain.invoke("Artificial Intelligence")
print(result)


title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Generate a blog title about {topic}"
)

title_chain = LLMChain(
    llm=llm,
    prompt=title_prompt
)

# Chain 2: Generate Paragraph
paragraph_prompt = PromptTemplate(
    input_variables=["title"],
    template="Write a short paragraph about this blog title:\n{title}"
)

paragraph_chain = LLMChain(
    llm=llm,
    prompt=paragraph_prompt
)

# Sequential Chain
chain = SimpleSequentialChain(
    chains=[title_chain, paragraph_chain],
    verbose=True
)

result = chain.invoke("Artificial Intelligence")

print("\nFinal Output:")
print(result)



from langchain_classic.chains import  SequentialChain


# -------------------------
# Chain 1: Title Generator
# -------------------------

title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Generate a catchy blog title on {topic}"
)

title_chain = LLMChain(
    llm=llm,
    prompt=title_prompt,
    output_key="title"
)

# -------------------------
# Chain 2: Outline Generator
# -------------------------

outline_prompt = PromptTemplate(
    input_variables=["title"],
    template="Create a blog outline for:\n{title}"
)

outline_chain = LLMChain(
    llm=llm,
    prompt=outline_prompt,
    output_key="outline"
)

# -------------------------
# Chain 3: Blog Generator
# -------------------------

blog_prompt = PromptTemplate(
    input_variables=["outline"],
    template="Write a blog article based on:\n{outline}"
)

blog_chain = LLMChain(
    llm=llm,
    prompt=blog_prompt,
    output_key="blog"
)

# -------------------------
# Final Sequential Chain
# -------------------------

final_chain = SequentialChain(
    chains=[
        title_chain,
        outline_chain,
        blog_chain
    ],
    input_variables=["topic"],
    output_variables=[
        "title",
        "outline",
        "blog"
    ],
    verbose=True
)

result = final_chain.invoke(
    {"topic": "Artificial Intelligence"}
)

print("\nTITLE:")
print(result["title"])

print("\nOUTLINE:")
print(result["outline"])

print("\nBLOG:")
print(result["blog"])




