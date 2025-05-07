import streamlit as st
from transformers import pipeline

st.title("✍️ AI Blog Generator")
topic = st.text_input("Enter your blog topic:")

if topic:
    generator = pipeline("text-generation", model="distilgpt2")
    with st.spinner("Generating..."):
        result = generator(topic, max_length=100, num_return_sequences=1)
        st.success("Here's your AI-generated blog snippet:")
        st.write(result[0]["generated_text"])

