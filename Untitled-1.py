"""
AI Agent From Scratch — No Framework, Just the Raw API
=========================================================
Yeh script dikhata hai ki agent loop ANDAR se kaise kaam karta hai —
bina LangChain/CrewAI jaise framework ke. Pehle isse samjho,
phir frameworks easy lagenge (wo bas isi pattern ko wrap karte hain).

Setup:
  pip install anthropic
  export ANTHROPIC_API_KEY="your-key-here"   (Mac/Linux)
  set ANTHROPIC_API_KEY="your-key-here"      (Windows cmd)

Run:
  python ai_agent_from_scratch.py
"""

import json
from anthropic import Anthropic

client = Anthropic()  # automatically reads ANTHROPIC_API_KEY from environment

# -------------------------------------------------------------
# STEP 1: Define the tools — yahi schema model ko dikhega
# -------------------------------------------------------------
tools = [
    {
        "name": "calculator",
        "description": "Evaluate a basic math expression. Use this for any arithmetic.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A math expression like '23 * 17' or '(45 + 5) / 2'",
                }
            },
            "required": ["expression"],
        },
    },
    {
        "name": "get_weather",
        "description": "Get the current weather for a given city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name, e.g. 'Ludhiana'"}
            },
            "required": ["city"],
        },
    },
]

# -------------------------------------------------------------
# STEP 2: Actual Python functions behind each tool
# -------------------------------------------------------------
def calculator(expression: str) -> str:
    try:
        # NOTE: eval() is unsafe for real production use — fine for this demo only.
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def get_weather(city: str) -> str:
    # Mock data — real version would call a weather API here.
    fake_db = {
        "ludhiana": "32°C, clear skies",
        "delhi": "38°C, hazy",
        "mumbai": "29°C, humid with light rain",
    }
    return fake_db.get(city.lower(), f"No data found for {city}")


# Dispatcher: tool ka naam -> actual function
TOOL_FUNCTIONS = {
    "calculator": lambda inp: calculator(inp["expression"]),
    "get_weather": lambda inp: get_weather(inp["city"]),
}


# -------------------------------------------------------------
# STEP 3: The Agent Loop (this IS the ReAct pattern)
# -------------------------------------------------------------
def run_agent(user_message: str, max_steps: int = 5):
    messages = [{"role": "user", "content": user_message}]

    for step in range(max_steps):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            tools=tools,
            messages=messages,
        )

        # Agar model ne final answer de diya (tool call nahi kiya), loop khatam
        if response.stop_reason != "tool_use":
            final_text = "".join(
                block.text for block in response.content if block.type == "text"
            )
            print(f"\n[Final Answer] {final_text}")
            return final_text

        # Model ne tool(s) call kiya hai — pehle uska response history mein add karo
        messages.append({"role": "assistant", "content": response.content})

        # Har tool_use block ko process karo (model ek baar mein multiple tools maang sakta hai)
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                tool_name = block.name
                tool_input = block.input
                print(f"[Step {step+1}] Agent is calling: {tool_name}({tool_input})")

                result = TOOL_FUNCTIONS[tool_name](tool_input)
                print(f"[Step {step+1}] Observation: {result}")

                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result),
                    }
                )

        # Tool ka result wapas model ko bhejo, taaki wo aage soch sake
        messages.append({"role": "user", "content": tool_results})

    print("Max steps reached without a final answer.")
    return None


# -------------------------------------------------------------
# STEP 4: Try it out
# -------------------------------------------------------------
if __name__ == "__main__":
    run_agent("What's the weather in Ludhiana, and what is 45 * 12 + 8?")