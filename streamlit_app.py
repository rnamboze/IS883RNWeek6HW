import streamlit as st
from openai import OpenAI
import os
from transformers import pipeline, set_seed

BUID = 48882893
set_seed(BUID)

### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key

prompt = st.text_input("How may I help you today?", "Damascus is")

generator = pipeline('text-generation', model='gpt2')
set_seed(42)
generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)


st.title("🤓My Amazing GPT2 App🤓")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
