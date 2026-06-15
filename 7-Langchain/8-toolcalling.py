import os
import requests

from dotenv import load_dotenv
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# ----------------------------------
# TOOL 1 : Weather Tool
# ----------------------------------

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    try:
        url = "http://api.weatherapi.com/v1/current.json"

        params = {
            "key": WEATHER_API_KEY,
            "q": city
        }

        response = requests.get(url, params=params)
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        return (
            f"Weather in {city}: "
            f"{temp}°C, {condition}"
        )

    except Exception as e:
        return f"Weather lookup failed: {str(e)}"


# ----------------------------------
# TOOL 2 : Currency Converter
# ----------------------------------

@tool
def currency_converter(query: str) -> str:
    """
    Convert currency.
    Example:
    '100 USD to INR'
    """

    try:

        parts = query.upper().split()

        amount = float(parts[0])
        from_currency = parts[1]
        to_currency = parts[3]

        url = f"https://open.er-api.com/v6/latest/{from_currency}"

        response = requests.get(url)
        data = response.json()

        rate = data["rates"][to_currency]

        converted = amount * rate

        return (
            f"{amount} {from_currency} = "
            f"{converted:.2f} {to_currency}"
        )

    except Exception as e:
        return f"Conversion failed: {str(e)}"

# Register the tools
tools = [
    get_weather,
    currency_converter
]

llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0.2
)

llm_with_tools = llm.bind_tools(tools)


# creating the agent loop
def run_assistant(user_query):

    response = llm_with_tools.invoke(
        [HumanMessage(content=user_query)]
    )

    # Check if model selected a tool
    if response.tool_calls:

        tool_call = response.tool_calls[0]

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        print(f"\nTool Selected: {tool_name}")

        selected_tool = next(
            tool for tool in tools
            if tool.name == tool_name
        )

        result = selected_tool.invoke(tool_args)

        print(f"\nTool Result:\n{result}")

        return result

    else:
        print(response.content)
        

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    run_assistant(user_input)