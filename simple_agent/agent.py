import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="tool_agent",
    model="gemini-flash-latest",
    instruction="Provide the most mind-blowing, obscure, and wacky fun facts about the topic. Aim for maximum 'wow' factor with rare and surprising information.",
    description="An Agent to provide fun facts about a given topic.",
    tools=[google_search],
)
