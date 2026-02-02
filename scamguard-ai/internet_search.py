import os
from typing import Literal
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

# 1️⃣ Get API key (string)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found in environment variables")

# 2️⃣ Create Tavily client (object)
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query=query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )

if __name__ == "__main__":
    result = internet_search(
        query= "General news",
        max_results=3,
        topic="general"
    )

    print("Search Results:")
    print(result)
