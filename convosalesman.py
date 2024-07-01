import streamlit as st
from streamlit_extras.colored_header import colored_header
from langchain.llms import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import datetime

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check for API key
if not GOOGLE_API_KEY:
    st.error("Please set your GOOGLE_API_KEY in the .env file.")
    st.stop()

# Configure Google Generative AI
google_genai = GoogleGenerativeAI(api_key=GOOGLE_API_KEY)

# Prompt Template (dynamically built based on user input)
template = """
You are a skilled sales scriptwriter and coach. A sales rep is looking to craft a cold call script. Based on the information provided so far:

{context}

Please ask the next logical question to help the sales rep build their script. Keep the question focused on gathering essential information for an effective cold call.
"""
prompt_template = PromptTemplate(
    input_variables=["context"],
    template=template,
)

def ai_chatbot(context):
    prompt = prompt_template.format(context=context)
    try:
        response = google_genai(prompt)
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, I'm having trouble understanding. Could you rephrase that?"
    return response

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Hi there! I'm your AI sales coach. Let's craft an awesome cold call script together. First, tell me about your product or service."})

# UI Design
st.set_page_config(page_title='Advi Script', layout='wide')

colored_header(label="Advi Script", description="AI Sales Coach", color_name="blue-70")
st.markdown("<style>div.stButton > button:first-child {background-color: #007bff; color: white;}</style>", unsafe_allow_html=True)

# Chat Display in Main Area
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            st.write(f"_{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}_")
        st.markdown(message["content"])

# User Input
with st.form(key="user_input", clear_on_submit=True):
    user_input = st.text_input("You:")
    if st.form_submit_button("Send"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Build context for the AI
        context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
        
        response = ai_chatbot(context)
        st.session_state.messages.append({"role": "assistant", "content": response})

        st.experimental_rerun()  # Refresh UI to show the new message
