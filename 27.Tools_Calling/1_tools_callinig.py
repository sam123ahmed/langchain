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

llm_with_tools.invoke("Hi how are you")
llm_with_tools.invoke("Can you multiply 3 with 10")

llm_with_tools.invoke("Can you multiply 3 with 10").tool_calls
llm_with_tools.invoke("Can you multiply 3 with 10").tool_calls[0]
