import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Set the model and chat history
model = st.session_state["openai_model"]
chat_history = st.session_state.messages

# Get user input
user_input = st.text_input("You:", "")

# Send user input to OpenAI
if st.button("Send"):
    if user_input:
        chat_history.append({"role": "user", "content": user_input})
        response = client.send_message(model, chat_history)
        chat_history.append({"role": "bot", "content": response})
        st.session_state.messages = chat_history
        
# Display chat history
for message in chat_history:
    st.text_area(message["role"].capitalize() + ": ", message["content"], height=100)
    
# Select a different model
st.sidebar.subheader("Select a different model")
model = st.sidebar.selectbox("Model", ["gpt-3.5-turbo", "gpt-4-turbo", "davinci-codex", "davinci-codex-beta"], index=0)
st.session_state["openai_model"] = model

# Clear chat history
if st.sidebar.button("Clear chat history"):
    st.session_state.messages = []
    
    

    