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
#load css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
st.title('Advi Script')
st.markdown("An AI-powered tool to generate tailored cold call scripts.")
st.markdown("Provide details about your target industry, preferred tone, script length, and keywords to get a customized script.")
st.markdown("**Example Keywords (comma-separated):** efficiency, cost savings, scalability")

# Sidebar Form for Input
with st.sidebar:
    with st.form("input_form"):
        form_choice = st.selectbox(
            "Select Industry:",
            ["Technology", "Healthcare", "Finance", "Manufacturing", "Retail", "Professional Services", "Real Estate", "Marketing", "Legal", "Automotive", "Construction", "Entertainment", "Education", "Hospitality", "Other"]
        )

        if form_choice == "Other":
            other_industry = st.text_input("Please specify the industry:")
            industry = other_industry if other_industry else form_choice
        else:
            industry = form_choice

        form_script_type = st.selectbox("Select Script Type:", ["Discovery Calls", "Cold Calls", "Elevator Pitches", "Remote Selling Scripts", "Product Demo Scripts", "Objection Handling Scripts", "Negotiation Scripts", "Referral Scripts", "Customer Storytelling Scripts"])
        form_tone = st.selectbox("Select Tone:", ["Professional and Trustworthy", "Casual and conversational", "Persuasive and Assertive", "Empathetic and Supportive", "Energetic and Enthusiastic", "Urgent and persuasive", "Friendly and approachable"])
        form_length = st.selectbox("Select Length:", ["Short", "Medium", "Long"])
        form_keywords = st.text_input("Enter 3 descriptive keywords (comma-separated):")

        submitted = st.form_submit_button("Generate Script")
        if submitted:
            st.write(f"Generating a {form_length} {form_script_type} script for a {industry} company with a {form_tone} tone.")
            st.session_state.messages.append({"role": "user", "content": industry})
            response = ai_chatbot(industry, form_tone.lower(), form_length.lower(), form_keywords)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Display Generated Script in the Main Area
if st.session_state.messages:
    st.markdown("### Generated Script")
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            st.markdown(message["content"])

# Button to copy generated script to clipboard
if st.button("Copy Script to Clipboard"):
    if st.session_state.messages:
        script_content = "\n".join([msg["content"] for msg in st.session_state.messages if msg["role"] == "assistant"])
        st.text_area("Generated Script", value=script_content, height=200)

# Button to clear chat history
if st.button("Clear Chat"):
    st.session_state.messages = []