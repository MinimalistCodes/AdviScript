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

#Conversational chatbot that will develop sales scripts for the user

#Conversation always on top. Chatbot speaks first
if st.session_state.messages == []:
    st.session_state.messages.append({"role": "assistant", "content": "Hello! I'm Advi Script, your AI-powered sales script assistant. How can I help you today?"})

#Display chat history
for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.text_area("Advi Script", message["content"], disabled=True, height=100)
    else:
        st.text_area("You", message["content"], disabled=True, height=100)
    

#User input
user_input = st.text_input("You", "What is the industry you are targeting?")
if st.button("Send"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": ai_chatbot(user_input)})
    st.session_state.messages.append({"role": "assistant", "content": "Is there anything else I can help you with?"})
    
#Clear chat history
if st.button("Clear Chat"):
    st.session_state.messages = []



