from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests

from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city"""
    url = f"weather data url&query={city}"

    response = requests.get(url)

    return response.json()

llm = ChatOpenAI()

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# step 2: Pull the react prompt from Langchain Hub
prompt = hub.pull("hwchase17/react") # pulls the standard react agent prompt

# step 3: create the react agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

# step 4: wrap it with agentexecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)


# step 5: Invoke
response = agent_executor.invoke({"input": "Find the capital of Madhya Pradesh, then find it's current weather condition"})
print(response)

response["output"]



