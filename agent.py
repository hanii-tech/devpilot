from google.adk.agents import SequentialAgent

from devpilot.agents.planner_agent import planner_agent
from devpilot.agents.research_agent import research_agent
from devpilot.agents.coding_agent import coding_agent
from devpilot.agents.review_agent import review_agent 
from devpilot.agents.documentation_agent import documentation_agent


root_agent = SequentialAgent(
    name="devpilot",
    description="An AI software engineering assistant that plans, researches, writes, and reviews codes.",
    sub_agents=[
        planner_agent,
        research_agent,
        coding_agent,
        review_agent,
        documentation_agent
    ]
)
