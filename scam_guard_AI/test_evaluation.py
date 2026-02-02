# creating a search agent


import os
from typing import Literal
from tavily import TavilyClient
from dotenv import load_dotenv
import streamlit as st

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

    #---------------UI------------------------------
st.set_page_config("Personalize – Auto Web Search", layout="wide")
st.title("🔍 Personalize – Auto Web Search")

query = st.text_input(
    "Search query",
    placeholder="Delhi air pollution"
)

topic = st.selectbox("Topic", ["news","general","finance"], index=1)
max_results = st.slider("Max results", 1, 10, 3)
include_raw = st.checkbox("Include raw content")

if query.strip():
    with st.spinner("Searching the web..."):
        try:
            results = internet_search(
                query=query,
                max_results=max_results,
                topic=topic,
                include_raw_content=include_raw,
            )

            #st.subheader("📄 Raw JSON Response")
            #st.json(results)

            if "results" in results:
                st.subheader("📰 Parsed Results")
                for i, item in enumerate(results["results"], 1):
                    with st.expander(f"{i}. {item.get('title', 'No title')}"):
                        st.write(item.get("content", "N/A"))
                        st.write("🔗", item.get("url"))

        except Exception as e:
            st.error(str(e))
else:
    st.info("Start typing to trigger search automatically 👆")