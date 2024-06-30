import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os, sys


# Load environment variables
load_dotenv()

# Configure Google Gemini API - Remove this section as we will use langchain
# google_genai = GoogleGenAI(api_key=os.getenv("GOOGLE_API_KEY"))
GOOLGE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Function to generate the cold call script
def cold_script(industry):
    return f"""
Please generate a cold call script tailored for a sales representative calling potential customers in the {industry} industry. Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""

# Function for AI chatbot interaction using langchain
def ai_chatbot(industry):
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))
    for script in llm.stream(cold_script(industry)):
        st.session_state.messages.append({"role": "assistant", "content": script})
        return script


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI and Chat Logic
st.set_page_config(page_title='Advi Script', layout='wide')
st.title('Advi Script')
st.markdown("An AI-powered chatbot designed to provide expert advice in the sales industry.")

# Form for selecting industry and sending user message to chatbot
with st.form("input_form"):
   #Add industries of common businesses
   #When "Other" is selected, show a inputbox for the industry name, show input box after its clicked before the button is pressed
   #ONLY submit when button is pressed
    industry = st.selectbox("Select Industry", ["Technology", "Finance", "Healthcare", "Real Estate", "Other"])
    if industry == "Other":
        industry = st.text_input("Enter Industry Name")
    submit_button = st.form_submit_button("Send")
    # If user message is submitted, add it to chat history and generate AI response
    if submit_button:
        st.session_state.messages.append({"role": "user", "content": industry})
        ai_chatbot(industry)



    
# Button to copy generated script to clipboard
if st.button("Copy Script to Clipboard"):
    if st.session_state.messages:
        script_content = "\n".join([msg["content"] for msg in st.session_state.messages if msg["role"] == "assistant"])
        st.text_area("Generated Script", value=script_content, height=200)

# Button to clear chat history
if st.button("Clear Chat"):
    st.session_state.messages = []


