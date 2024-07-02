import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
#save to pdf
#save to docx


from dotenv import load_dotenv
import os, sys

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def ai_sales_coach(user_input):
    prompt = f"""
    You are an expert sales coach. You can help with various aspects of sales, including:

    *   Generating cold call scripts
    *   Crafting effective email templates
    *   Providing advice on handling objections
    *   Offering tips for closing deals
    *   Suggesting strategies for prospecting and lead generation
    *   Guiding sales presentations and demos
    *   Sharing best practices for building customer relationships
    *   Explaining sales methodologies and frameworks
    *   Assisting with sales training and coaching
    *   Team building and motivation
    *   Sales management and leadership
    *   Tracking and analyzing sales performance
    *   Sales exercises and role-playing scenarios
    *   Sales forecasting and pipeline management
    *   Sales negotiation tactics and strategies
    *   Recommendations for sales technology and tools
    *   Sales psychology, buyer behavior, and persuasion techniques
    *   Sales ethics and compliance
    *   Emotional intelligence in sales

    Please provide a comprehensive response to the following request:

    {user_input}
    """
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    return llm.invoke(prompt)


# UI Layout
st.title("Advi Script - Your AI Sales Coach")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")

# Custom CSS for basic styling (you can customize this further)
st.markdown("""
<style>
.chat-message {
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 10px;
    line-height: 1.5;
}
.user-message {
    background-color: #F0F0F0;
    text-align: right;
}
.bot-message {
    background-color: #FFFFFF;
    text-align: left;
}
#chat-input-container {
    padding: 15px;
}
#chat-input {
    width: calc(100% - 30px);
    resize: vertical;
    min-height: 40px; 
    max-height: 200px; 
}
</style>
""", unsafe_allow_html=True)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = ai_sales_coach(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})