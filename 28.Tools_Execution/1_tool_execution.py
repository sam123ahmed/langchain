import os
os.environ["test"] = ""

# !pip install -q langchain-openai langchain-core requests

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

# tool create
@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b

print(multiply.invoke({"a": 3, "b": 4}))

multiply.name
multiply.description
multiply.args



# tool binding
llm = ChatOpenAI()
llm_with_tools = llm.bind_tools([multiply])

# tool calling
llm_with_tools.invoke("Hi how are you")

query = HumanMessage("Can you multiply 3 with 10")

messages = [query]
messages

# llm_with_tools.invoke("Can you multiply 3 with 10")

# llm_with_tools.invoke("Can you multiply 3 with 10").tool_calls
# llm_with_tools.invoke("Can you multiply 3 with 10").tool_calls[0]


result = llm_with_tools.invoke(messages)
messages.append(result)
messages

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)
messages

llm_with_tools.invoke(messages)
llm_with_tools.invoke(messages).content


# result.tool_calls[0]["args"]
# # tool execution
# multiply.invoke(result.tool_calls[0]["args"])
# multiply.invoke(result.tool_calls[0])