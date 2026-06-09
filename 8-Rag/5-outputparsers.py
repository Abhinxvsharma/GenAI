
from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser,
    CommaSeparatedListOutputParser,
)
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

# ---------------------------------------------------
# 1. Initialize LLM
# ---------------------------------------------------

llm = ChatOllama(
    model="phi3:mini",
    temperature=0.5
)

# ===================================================
# STRING OUTPUT PARSER
# ===================================================

# print("\n" + "=" * 50)
# print("STRING OUTPUT PARSER")
# print("=" * 50)

# string_parser = StrOutputParser()

# string_prompt = PromptTemplate(
#     template="What is the capital of {country}?",
#     input_variables=["country"]
# )

# string_chain = string_prompt | llm | string_parser

# result = string_chain.invoke({"country": "France"})

# print("Output:")
# print(result)


# ===================================================
# LIST OUTPUT PARSER
# ===================================================

# print("\n" + "=" * 50)
# print("LIST OUTPUT PARSER")
# print("=" * 50)

# list_parser = CommaSeparatedListOutputParser()

# list_prompt = PromptTemplate(   
#     template="""  
# Give 5 popular programming languages.  

# {format_instructions}
# """,
#     input_variables=[],
#     partial_variables={
#         "format_instructions": list_parser.get_format_instructions()
#     },
# )

# list_chain = list_prompt | llm | list_parser

# result = list_chain.invoke({})

# print("Output:")
# print(result)
# print("Type:", type(result))


# ===================================================
# JSON OUTPUT PARSER
# ===================================================

# print("\n" + "=" * 50)
# print("JSON OUTPUT PARSER")
# print("=" * 50)

# json_parser = JsonOutputParser()

# json_prompt = PromptTemplate(
#     template="""
# Provide information about a student.

# Return ONLY valid JSON.

# {format_instructions}

# Student Name: John
# Age: 21
# Course: Data Science
# """,
#     input_variables=[],
#     partial_variables={
#         "format_instructions": json_parser.get_format_instructions()
#     },
# )

# json_chain = json_prompt | llm | json_parser

# result = json_chain.invoke({})

# print("Output:")
# print(result)
# print("Type:", type(result))


# # ===================================================
# # PYDANTIC OUTPUT PARSER
# # ===================================================

from langchain_core.output_parsers import PydanticOutputParser

print("\n" + "=" * 50)
print("PYDANTIC OUTPUT PARSER")
print("=" * 50)

class Employee(BaseModel):
    name: str = Field(description="Employee name")
    age: int = Field(description="Employee age")
    department: str = Field(description="Employee department")

pydantic_parser = PydanticOutputParser(
    pydantic_object=Employee
)

pydantic_prompt = PromptTemplate(
    template="""
Generate employee information.

IMPORTANT:
Return ONLY valid JSON.
Do not include explanations.
Do not include markdown.
Do not include ```json.

{format_instructions}


""",
    input_variables=[],
    partial_variables={
        "format_instructions":
            pydantic_parser.get_format_instructions()
    },
)

pydantic_chain = (
    pydantic_prompt
    | llm
    | pydantic_parser
)

result = pydantic_chain.invoke({})

print("Output:")
print(result)
print("Name:", result.name)
print("Age:", result.age)
print("Department:", result.department)



