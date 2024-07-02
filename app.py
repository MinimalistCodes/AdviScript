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


# UI and Chat Logic
st.title('Advi Script - Your AI Sales Coach')
st.sidebar.markdown("**Chat History**")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")

# Custom CSS for ChatGPT-like styling
st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #F8F9FA; /* Light background */
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    overflow-y: auto;
    max-height: 500px; 
}
.chat-container {
    background-color: #FFFFFF; /* White background for main chat area */
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    overflow-y: auto; /* Enable scrolling */
    max-height: 500px;  /* Set maximum height */
}
.user-message, .bot-message {
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
}
.user-message {
    background-color: #E2F0FF; /* Light blue */
    text-align: right;
}
.bot-message {
    background-color: #F0F0F0; /* Light gray */
    text-align: left;
}

.typing-indicator {
    color: #999999; /* Gray color for the typing indicator */
    font-size: 12px;
    margin-top: -10px; /* Adjust as needed for spacing */
}
.chat-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
    cursor: pointer; /* Make card clickable */
}
.chat-card:hover {
    background-color: #f5f5f5; /* Light gray on hover */
}

#chat-input-container {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #F8F9FA; /* Match the background of the chat area */
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# Chat History in Sidebar
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar.container(): 
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Main Chat Area
with st.container():  
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Input Box at the Bottom (Outside the Container)
with st.container():
    user_input = st.chat_input("Your message", key="chat_input")

if user_input:  
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Display "Sales Coach is typing..." message
    with st.chat_message("assistant"):
        message_placeholder = st.empty() 
        message_placeholder.markdown("Sales Coach is typing...")

    # Get AI response with a slight delay to simulate typing
    time.sleep(1)  # Adjust delay as needed
    response = ai_sales_coach(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Clear the typing indicator
    message_placeholder.markdown(response) 