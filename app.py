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

    *   Generating all types of sales scripts
    *   Providing sales call scripts and phone sales tips
    *   Offering advice on handling objections and rejections
    *   Giving tips for closing deals and overcoming sales objections
    *   Suggesting strategies for prospecting and lead generation
    *   Guiding sales presentations and demos
    *   Crafting effective email templates
    *   Offering tips for closing deals
    *   Suggesting strategies for prospecting and lead generation
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


# UI Layout (Gemini-inspired, full-screen chat, input at bottom)
st.title("Advi Script - Your AI Sales Coach")

# Custom CSS for Gemini-like styling with docked input
st.markdown("""
<style>
body {
    font-family: 'Arial', sans-serif;
    background-color: #F8F9FA; /* Background for entire page */
}
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
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #FFFFFF;
    padding: 15px;
}
#chat-input {
    width: calc(100% - 30px);
    resize: vertical;
    min-height: 40px;
    max-height: 200px;
}
#chat-messages-container {
    padding-bottom: 80px; /* Adjust based on input container height */
    overflow-y: auto;
}
</style>
""", unsafe_allow_html=True)

# Chat History and AI Responses
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.container():
    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Input Box at the Bottom (Docked and Centered)
with st.container():
    user_input = st.text_area("Your message", key="chat_input", height=40, on_submit=ai_sales_coach(user_input))

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Display "Sales Coach is typing..." message
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Sales Coach is typing...")

    # Get AI response with a slight delay to simulate typing
    time.sleep(1)
    response = ai_sales_coach(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Clear the typing indicator and display the response
    message_placeholder.markdown(response)

    # Clear the input box after sending the message
    st.session_state.chat_input = ""