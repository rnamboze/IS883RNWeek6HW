import streamlit as st
from openai import OpenAI
import os
from transformers import pipeline, set_seed

BUID = 48882893
set_seed(BUID)

### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key

### Request the answer to the question "How may I help you?"
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-2",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": "Damascus is a"}
  ],
  n=10,
  max_tokens=20
)

### Print all 10 completions:
for i in range(10):
  st.write(response.choices[i].message.content)

st.title("🤓My Amazing GPT2 App🤓")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
