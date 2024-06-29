import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from IPython.display import Markdown
import textwrap

# Load environment variables from .env file (if you are using a .env file to store your API key)
load_dotenv()

# Initialize Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-pro")

# Function to generate the cold call script
def cold_script(industry):
    return f"""
Please generate a cold call script tailored for a sales representative calling potential customers in the {industry} industry. Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""

# Function to format text as Markdown with indentation
def to_markdown(text):
    text = text.replace('•', '  *')
    text = text.replace('\n', '<br>')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function for AI chatbot interaction
def ai_chatbot(message):
    prompt = cold_script(message)  # Assuming message here is the industry
    response = model.generate_content(prompt)
    return to_markdown(response)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI and Chat Logic
st.set_page_config(page_title='Advi Script', layout='wide')
st.title('Advi Script')
st.markdown("An AI-powered chatbot designed to provide expert advice in the sales industry.")

# Display chat messages in a full-width container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.markdown(f'<div class="message assistant">{message["content"]}</div>', unsafe_allow_html=True)
    elif message["role"] == "user":
        st.markdown(f'<div class="message user">{message["content"]}</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# User input for sending direct messages to the chatbot
user_input = st.text_input("You:", key="user_input")

# Send user message to chatbot
if st.button("Send"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = ai_chatbot(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat history button
if st.button("Clear Chat"):
    st.session_state.messages = []
