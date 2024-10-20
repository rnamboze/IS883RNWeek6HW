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

### OpenAI stuff
client = OpenAI()
response = client.chat.completions.create(
  model="gpt2",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
)

### Display
st.write(
    response.choices[0].message.content
)

st.title("🤓My Amazing GPT2 App🤓")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
