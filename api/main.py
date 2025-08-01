import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain.memory import ConversationBufferMemory
from config import OPENWEATHER_API_KEY, OPENWEATHER_API_URL, OPENWEATHER_UNITS, OPENWEATHER_LANG

load_dotenv()

def get_weather(city: str) -> str:
    url = OPENWEATHER_API_URL
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": OPENWEATHER_UNITS,
        "lang": OPENWEATHER_LANG
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"{city}: {temp}°C, {description}"
    except Exception as e:
        return f"Error while retrieving weather for {city}: {str(e)}"

weather_tool = Tool(
    name="get_weather",
    func=get_weather,
    description="Returns the current weather (temperature and description) for a city. You must use this tool whenever the user asks about weather. Input: city name in English, e.g., 'Tokyo'."
)

chat_history = FileChatMessageHistory("../chat_history.json")

memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=chat_history,
    return_messages=True
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

class AgentQuery(BaseModel):
    query: str

# POST /ask endpoint
@app.post("/ask")
async def ask_agent(request: AgentQuery):
    result = agent.invoke(request.query)
    return {"response": result["output"]}