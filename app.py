import streamlit as st
from langchain_google_genai import GoogleGenerativeAI


from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google Gemini API - Remove this section as we will use langchain
# google_genai = GoogleGenAI(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate the cold call script
def cold_script(industry):
    return f"""
Please generate a cold call script tailored for a sales representative calling potential customers in the {industry} industry. Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""

# Function for AI chatbot interaction using langchain
def ai_chatbot(industry):
    prompt = cold_script(industry)
    llm = GoogleGenerativeAI(model="gpt-3.5-turbo", api_key=os.getenv("GOOGLE_API_KEY"))
    response = llm.invoke(prompt)
    return response

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI and Chat Logic
st.set_page_config(page_title='Advi Script', layout='wide')
st.title('Advi Script')
st.markdown("An AI-powered chatbot designed to provide expert advice in the sales industry.")

# Display chat messages
for message in st.session_state.messages:
    st.markdown(f'**{message["role"]}**: {message["content"]}')

# User input for sending direct messages to the chatbot
user_input = st.text_input("You:", key="user_input")

# Form for selecting industry and sending user message to chatbot
with st.form("input_form"):
    form_choice = st.selectbox(
        "Select Industry:",
        ["Technology", "Finance", "Healthcare", "Education", "Sales", "Other"]
    )

    if form_choice == "Other":
        other_industry = st.text_input("Please specify the industry:")
        industry = other_industry if other_industry else form_choice
    else:
        industry = form_choice

    submitted = st.form_submit_button("Send")
    if submitted:
        st.write(f"Generating a cold call script for the {industry} industry...")
        st.session_state.messages.append({"role": "user", "content": industry})
        response = ai_chatbot(industry)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Button to copy generated script to clipboard
if st.button("Copy Script to Clipboard"):
    if st.session_state.messages:
        script_content = "\n".join([msg["content"] for msg in st.session_state.messages if msg["role"] == "assistant"])
        st.text_area("Generated Script", value=script_content, height=200)

# Button to clear chat history
if st.button("Clear Chat"):
    st.session_state.messages = []

# Function to generate text using langchain
def generate_text(prompt):
    from langchain import LangChain

    # Initialize LangChain with appropriate settings
    lc = LangChain(provider="google", api_key=os.getenv("GOOGLE_API_KEY"))  # Adjust provider and configuration as needed

    # Generate text
    response = lc.generate_text(prompt)
    return response

