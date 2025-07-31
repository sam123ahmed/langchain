# !pip install langchain langchain-core langchain-community pydantic duckduckgo-search langchain-experimental


# Built-in Tool - DuckDuckGo Search
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke("ipl news")
print(results)




# Built-in Tool - Shell Tool
from langchain_community.tools import ShellTool

shell_tool = ShellTool()

results = shell_tool.invoke("whoami")
print(results)