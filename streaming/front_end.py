import streamlit as st
import requests

st.set_page_config(page_title="Backend Streaming Test")

st.title("FastAPI Streaming Test (LangGraph Backend)")

topic = st.text_input(
    "Enter a blog topic",
    "Generative AI Jobs Prediction in Bangladesh for 2026"
)

if st.button("Stream from backend"):

    url = f"http://localhost:8010/chat/{topic}"

    response = requests.get(url, stream=True)

    output_box = st.empty()
    streamed_text = ""

    for chunk in response.iter_content(chunk_size=None):
        if chunk:
            token = chunk.decode("utf-8")
            streamed_text += token
            output_box.markdown(streamed_text)
