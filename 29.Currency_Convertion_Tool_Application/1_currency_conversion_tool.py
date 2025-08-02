import requests
from langchain_core.tools import tool, InjectedToolArg
from typing import Annotated

# tool create
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    This function fetches the currency conversion factor between a given base currency and a target currency
    """
    url = f"https://v6.exchangerate-api.com/v6/656df3e3d0568c72213dcd1d/pair/{base_currency}/{target_currency}"

    response = requests.get(url)
    return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """Given a currency conversion rate this function calculates the target currency value from a given base currency value"""
    return base_currency_value * conversion_rate



get_conversion_factor.invoke({"base_currency": "USD", "target_currency": "INR"})
convert.invoke({"base_currency_value": 10, "conversion_rate": 87.16})

# tool binding
llm = ChatOpenAI()

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

messages = [HumanMessage("What is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr")]
messages


ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)
ai_message.tool_calls

import json
for tool_call in ai_message.tool_calls:
    # execute the first tool and get the value of conversion rate
    if tool_call["name"] == "get_conversion_factor":
        tool_message1 = get_conversion_factor.invoke(tool_call)
        # fetch this conversion rate
        conversion_rate = json.loads(tool_message1.content)["conversion_rate"]
        # append this tool message to messages list
        messages.append(tool_message1)
    # execute the second tool using the conversion rate from tool
    if tool_call["name"] == "convert":
        # fetch the current arg
        tool_call["args"]["conversion_rate"] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)


messages

llm_with_tools.invoke(messages).content