import streamlit as st
from langchain_google_genai import GoogleGenerativeAI


from dotenv import load_dotenv
import os, sys

# Load environment variables
load_dotenv()

# Configure Google Gemini API - Remove this section as we will use langchain
api_key = os.getenv("GOOGLE_API_KEY")


# Function to generate the cold call script
def cold_script(industry, keywords, length, tone, script_type):
    return f"""
Please generate a {script_type} script for a {industry} company that specializes in {keywords}.
The script should be tailored to a {tone} tone and a {length} length. 
Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. 
The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""


# Function for AI chatbot interaction using langchain
def ai_chatbot(industry, keywords="", length="medium", tone="conversational", script_type=""):
    prompt = cold_script(industry, keywords, length, tone, script_type)
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    st.write(llm.invoke(prompt))

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI and Chat Logic
st.set_page_config(page_title='Advi Script', layout='wide')
st.title('Advi Script')

# Main Area for Displaying the Chat
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Sidebar Form for Input
with st.sidebar:
    st.markdown("An AI-powered tool to generate tailored cold call scripts.")
    st.markdown("Provide details about your target industry, preferred tone, script length, and keywords to get a customized script.")
    st.markdown("**Example Keywords (comma-separated):** efficiency, cost savings, scalability")

    with st.form("input_form"):
        # ... (Industry, Tone, Length, Keyword selection remains the same)

        submitted = st.form_submit_button("Generate Script")
        if submitted:
            keywords_list = [keyword.strip() for keyword in form_keywords.split(",")]
            response = ai_chatbot(industry, form_tone.lower(), form_length.lower(), form_keywords)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Update the chat display in the main area after each new message
if submitted:
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


# Copy and Clear Buttons (placed outside the form)
if st.session_state.messages and st.button("Copy Script to Clipboard"):
    script_content = "\n".join([msg["content"] for msg in st.session_state.messages if msg["role"] == "assistant"])
    st.text_area("Generated Script", value=script_content, height=200)

if st.button("Clear Chat"):
    st.session_state.messages = []