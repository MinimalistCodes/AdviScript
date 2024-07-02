import streamlit as st
from langchain.llms import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Function to generate the cold call script (no changes here)
def cold_script(industry, keywords, length, tone, script_type):
    # ... (same as your provided code)

# AI Chatbot Function (modified for chat interaction)
def ai_chatbot(user_input):
    if user_input.lower().startswith("generate"):
        # Extract details from user input
        try:
            _, industry, keywords, length, tone, script_type = user_input.split(", ")
        except ValueError:
            st.error("Please provide all details in this format: 'generate, industry, keywords, length, tone, script_type'")
            return "Error: Invalid input format."
        
        prompt = cold_script(industry, keywords, length, tone, script_type)
        llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
        return llm.invoke(prompt)
    else:
        return "Please start your request with 'generate' followed by a comma and then provide industry, keywords, length, tone, and script_type (e.g., 'generate, Technology, efficiency, cost savings, scalability, medium, professional')."

# UI and Chat Logic
st.title('Advi Script - Conversational Chatbot')
st.markdown("Chat with the AI to generate tailored cold call scripts. Use the format: 'generate, industry, keywords, length, tone, script_type'.")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = ai_chatbot(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
