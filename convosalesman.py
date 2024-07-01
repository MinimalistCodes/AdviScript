import streamlit as st
from streamlit_extras.colored_header import colored_header
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check for API key
if not GOOGLE_API_KEY:
    st.error("Please set your GOOGLE_API_KEY in the .env file.")
    st.stop()

llm = GoogleGenerativeAI(temperature=0, google_api_key=GOOGLE_API_KEY)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you create an awesome cold call script?"}
    ]

# Prompt Template
def get_template(messages):
    formatted_messages = ""
    for message in messages:
        formatted_messages += f"{message['role']}: {message['content']}\n"
    return formatted_messages

# App UI
st.set_page_config(page_title='SalesGPT')

st.header("SalesGPT - Your AI Sales Script Assistant")
st.markdown("Start typing below to create your sales script.")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Your input"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate AI response using the prompt template
    with st.chat_message("assistant"):
        response = llm(get_template(st.session_state.messages))
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)

# Copy Button
if st.session_state.messages and st.button("Copy Script"):
    script_content = "\n".join(
        [msg["content"] for msg in st.session_state.messages if msg["role"] == "assistant"]
    )
    st.code(script_content, language="text")
    st.toast("Script copied to clipboard!")
