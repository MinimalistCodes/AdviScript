import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-pro")

# Initialize Streamlit app title
st.title("Advi Script: AI-powered Sales Script Generator")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.expander(message["role"], expanded=True):
        st.markdown(message["content"])

# Input box for user messages
if prompt := st.text_input("You:", key="user_input"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.expander("user", expanded=True):
        st.markdown(prompt)

    # Generate AI response using Google Gemini API
    response = ai_chatbot(prompt)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.expander("assistant", expanded=True):
        st.markdown(response)

# Function to simulate AI response (using Google Gemini API)
def ai_chatbot(message):
    prompt = cold_script(message)
    response = model.generate_text(prompt, max_length=100, temperature=0.5)
    return response

# Function to generate cold call script based on industry input
def cold_script(industry):
    return f"""
Please generate a cold call script tailored for a sales representative calling potential customers in the {industry} industry. Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""
