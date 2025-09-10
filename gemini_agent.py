from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# (Optional) verify GEMINI_API_KEY is loaded
gemini_api_key = os.getenv("GOOGLE_API_KEY")
if not gemini_api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Initialize the Gemini model (API key picked automatically from environment)
gemini_model = Gemini(id="gemini-1.5-flash")  

# Web Agent
web_agent = Agent(
    name="Web Agent",
    model=gemini_model,
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=gemini_model,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Team Agent combining Web + Finance Agents
agent_team = Agent(
    model=gemini_model,
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Execute query through the team
agent_team.print_response(
    "Summarize analyst recommendations and share the latest news for NVDA", 
    stream=True
)
