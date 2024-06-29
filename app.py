import streamlit as st
from google.generativeai import TextService, types  
from google.api_core import retry
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Gemini
api_key = os.getenv("GOOGLE_API_KEY")
client = TextService(api_key=api_key)
model = types.Model("models/chat-bison-001")  

# Function to generate the cold call script
def cold_script(industry):
    return f"""
Please generate a cold call script tailored for a sales representative calling potential customers in the {industry} industry. Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""

# Function for AI chatbot interaction
def ai_chatbot(message):
    prompt = cold_script(message)
    response = client.generate_text(
        model=model,
        prompt=types.Prompt(
            text=prompt
        ),
        temperature=0.5,  
        max_output_tokens=1024 
    )
    return response.text

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
    response = ai_chatbot(industry)  
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
