import os
# !pip install -q langchain-openai langchain-community langchain-core requests duckduckgo-search

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke("top news in india today")
results

llm = ChatOpenAI()

llm.invoke("hi")


from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# step 2: Pull the react prompt from langchain hub
prompt = hub.pull("hwchase17/react") # pulls the standard react agent prompt


# step 3: create the react agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)


# step 4: wrap it with Agentexecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

# step 5: Invoke
response = agent_executor.invoke({"input": "3 ways to reach goa from delhi"})
print(response)

response["output"]
