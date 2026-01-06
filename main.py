from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

# class Source(BaseModel):
#     """Schema for a source used by the agent"""

#     url: str = Field(description="The URL of the source")


# class AgentResponse(BaseModel):
#     """Schema for agent response with answer and sources"""

#     answer: str = Field(description="Thr agent's answer to the query")
#     sources: List[Source] = Field(
#         default_factory=list, description="List of sources used to generate the answer"
#     )


llm = ChatOllama(temperature=0, model="llama3.1:8b")
tools = [TavilySearch(
    max_results=3
)]
agent = create_agent(model=llm, tools=tools, system_prompt="""
    You are a research agent.
    Use the provided search tool exactly as given.
    DO NOT add date filters or parameters that are not required.
    """)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(content="search for 3 job posting for ai engineers using langchain in the bay area and on linkedin and list thier details" )
            ]
        }
    )
    print(result)


if __name__ == "__main__":
    main()
