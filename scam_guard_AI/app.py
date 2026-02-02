import streamlit as st
from scam_classifier import build_scam_classifier_chain
from internet_search import internet_search
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="ScamGuard AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ ScamGuard AI")
st.subheader("Detect scam messages using Generative AI")

st.write(
    "Paste a message below to check whether it is a scam, not a scam, or uncertain."
)

user_input = st.text_area(
    "Enter message",
    height=150,
    placeholder="Example: Your bank account will be suspended. Click this link immediately."
)

if st.button("Analyze Message"):
    if not user_input.strip():
        st.warning("Please enter a message.")
    else:
        with st.spinner("Analyzing..."):
            chain = build_scam_classifier_chain()
            result = chain.invoke(
                {"user_message": user_input}
            )

        st.success("Analysis Complete")

        st.markdown("### 🔍 Classification")
        st.write(result.classification)

        st.markdown("### intent")
        st.write(result.intent_type)

        st.markdown("### 🧠 Reasoning")
        st.write(result.reasoning)

#--------UI for web search-----------------
# -------------------------------
# Session state initialization
# -------------------------------
if "query" not in st.session_state:
    st.session_state.query = ""

if "results" not in st.session_state:
    st.session_state.results = None

# -------------------------------
# Callback function
# -------------------------------
def run_search():
    query = st.session_state.query.strip()

    # Prevent useless calls
    if len(query) < 5:
        st.session_state.results = None
        return

    with st.spinner("🔍 Searching scam-related news..."):
        try:
            st.session_state.results = internet_search(
                query=query,
                max_results=st.session_state.max_results,
                topic=st.session_state.topic,
                include_raw_content=st.session_state.include_raw,
            )
        except Exception as e:
            st.error(str(e))
            st.session_state.results = None


# -------------------------------
# UI Controls
# -------------------------------
st_autorefresh(interval=300_000, key="scam_refresh")

# ----------------------------------
# 🔎 Auto scam search configuration
# ----------------------------------
AUTO_QUERY = (
    "latest scam SMS fraud India OR phishing message OR OTP scam "
    "OR fake delivery message OR banking fraud"
)

TOPIC = "news"
MAX_RESULTS = 5
INCLUDE_RAW = False

st.title("🚨 Live Scam News Monitor")
st.caption("Automatically tracking latest scam messages & fraud trends")

# ----------------------------------
# 🔍 Auto Search
# ----------------------------------
with st.spinner("Fetching latest scam intelligence..."):
    try:
        results = internet_search(
            query=AUTO_QUERY,
            max_results=MAX_RESULTS,
            topic=TOPIC,
            include_raw_content=INCLUDE_RAW,
        )

        if "results" in results and results["results"]:
            st.subheader("📰 Latest Scam Reports")
            for i, item in enumerate(results["results"], 1):
                with st.expander(f"{i}. {item.get('title', 'No title')}"):
                    st.write(item.get("content", "N/A"))
                    st.write("🔗", item.get("url"))
        else:
            st.warning("No scam-related news found at the moment.")

    except Exception as e:
        st.error(f"Search failed: {e}")