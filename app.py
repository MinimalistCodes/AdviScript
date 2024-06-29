import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

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

# Function for AI chatbot interaction
def ai_chatbot(message):
    prompt = cold_script(message) # Assuming message here is the industry
    response = model.generate_text(prompt)  # Increased max_length
    return response

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI and Chat Logic
st.title("AdviScript: AI-Powered Sales Script Generator")
st.write("Select industry and start chatting to generate a cold call script.")

with st.form("input_form"):
    industry = st.selectbox(
        "Select Industry:",
        ["Technology", "Finance", "Healthcare", "Education", "Other"]
    )
    submitted = st.form_submit_button("Generate Script")
if submitted:
    script_type = cold_script(industry)
    response = ai_chatbot(script_type)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.text_input("You:", key="user_input")

# Send user message to chatbot
if st.button("Send"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = ai_chatbot(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat history
if st.button("Clear Chat"):
    st.session_state.messages = []

