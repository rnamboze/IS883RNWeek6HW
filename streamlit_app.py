import streamlit as st
from openai import OpenAI
import os
from transformers import pipeline, set_seed

BUID = 48882893
set_seed(BUID)

### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key

### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')


### Generate the answer to the question "Damascus is a"
generator("Damascus is a", max_length=20, num_return_sequences=10, truncation=True)

st.title("🤓My Amazing GPT2 App🤓")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
