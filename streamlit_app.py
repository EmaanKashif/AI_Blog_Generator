import streamlit as st
from transformers import pipeline, set_seed

st.set_page_config(page_title="AI Blog Generator", page_icon="✍️", layout="centered")

st.title("✍️ AI Blog Generator")

st.markdown("""
Welcome! This tool helps you write blog content in seconds.  
Just tell the AI what your blog is about, and it will write a short piece for you.  
It’s like having a writing buddy who never runs out of ideas.
""")

st.header("💡 What’s your blog topic?")
topic = st.text_input("Type your topic here:")

st.sidebar.title("✏️ Make it your way")
max_length = st.sidebar.slider("How long should the blog be?", 50, 500, 150, 10)
temperature = st.sidebar.slider("How creative should it sound?", 0.5, 1.5, 1.0, 0.1)
seed = st.sidebar.number_input("Randomness (optional)", 0, 9999, 42, 1)

@st.cache_resource(show_spinner=False)
def load_writer():
    return pipeline("text-generation", model="gpt2-medium")

writer = load_writer()

if topic:
    set_seed(seed)
    with st.spinner("Thinking... Writing your blog..."):
        output = writer(
            topic,
            max_length=max_length,
            num_return_sequences=1,
            temperature=temperature,
            pad_token_id=50256
        )

    final_text = output[0]['generated_text'].strip()

    st.success("Done! Here’s your blog draft:")
    st.write(final_text)

    st.text_area("You can copy or edit your blog here:", value=final_text, height=250)
else:
    st.info("Please type a topic to get started. The AI is ready when you are!")


