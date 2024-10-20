import streamlit as st
from openai import OpenAI
import os
from transformers import pipeline, set_seed

BUID = 48882893
set_seed(BUID)

### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key

st.title("🤓My Amazing GPT2 App🤓")


prompt = st.text_input("What is your prompt today?", "Damascus is")

### Load your API Key
os.environ["OPENAI_API_KEY"] = st.secrets["OpenAIkey"]

### OpenAI stuff
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
)

### Display
st.write(
    response.choices[0].message.content
)


