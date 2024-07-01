import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
#save to pdf
#save to docx


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

def load_chat_history(chat_title):
    chat_history = []
    with open(f"chat_logs/{chat_title}.txt", "r") as file:
        for line in file:
            role, content = line.strip().split(":")
            chat_history.append({"role": role, "content": content})
    return chat_history


# Function for AI chatbot interaction using langchain
def ai_chatbot(industry, keywords="", length="medium", tone="conversational", script_type=""):
    prompt = cold_script(industry, keywords, length, tone, script_type)
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    st.write(llm.invoke(prompt))


# UI and Chat Logic
st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)
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
            with chat_container:
                st.write(f"Generating a {form_length} {form_script_type} script for a {industry} company with a {form_tone} tone.")
                st.session_state.messages.append({"role": "user", "content": industry})
                response = ai_chatbot(industry, form_tone.lower(), form_length.lower(), form_keywords)
                st.session_state.messages.append({"role": "assistant", "content": response})
    #Automatically save the chat history to a file
    save_chat = st.button("Save Chat History")
    if save_chat:
        with open("chat_logs/chat_history.txt", "w") as file:
            for message in st.session_state.messages:
                file.write(f"{message['role']}:{message['content']}\n")
                
        
   
                        
