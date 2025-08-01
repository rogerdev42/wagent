import os
import streamlit as st
import requests

API_HOST = os.getenv("API_HOST", "http://api:8000")

st.set_page_config(page_title="Weather AI Agent")

st.title("Weather AI Agent")
st.markdown("Ask about the weather — for example: **What's the weather in Tokyo?**")


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Enter your question..."):
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            res = requests.post(f"{API_HOST}/ask", json={"query": user_input})
            res.raise_for_status()
            output = res.json()["response"]
        except Exception as e:
            output = f"❌ Error contacting the agent: {e}"

        st.markdown(output)
        st.session_state.messages.append({"role": "assistant", "content": output})