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

    try:
        response = tavily_client.search(
            query=query,
            max_results=max_results,
            include_raw_content=include_raw_content,
            topic=topic,
        )

        # ✅ Detect quota / API failure responses
        if isinstance(response, dict) and response.get("error"):
            print("\n⚠ Tavily API Error:", response["error"])
            print("⚡ Switching to demo fallback mode...\n")

            return {
                "results": [
                    {
                        "title": "Demo Result – Tavily Credits Exhausted",
                        "url": "https://example.com",
                        "content": "Fallback response because API quota was exceeded."
                    }
                ]
            }

        return response

    except Exception as e:
        print("\n⚠ Tavily Exception:", str(e))
        print("⚡ Switching to demo fallback mode...\n")

        return {
            "results": [
                {
                    "title": "Demo Result – Search Unavailable",
                    "url": "https://example.com",
                    "content": "Fallback response due to request failure."
                }
            ]
        }

