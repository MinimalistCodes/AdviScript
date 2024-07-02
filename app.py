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
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")

# Custom CSS for ChatGPT-like styling
st.markdown("""
<style>
body {
    font-family: 'Arial', sans-serif; 
    display: flex; /* Use flexbox for layout */
    flex-direction: column; /* Arrange elements vertically */
    height: 100vh; /* Make the container take up full viewport height */
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
#chat-input { /* Style the textarea for input */
    width: calc(100% - 120px); /* Account for padding and button */
    resize: vertical; /* Allow vertical resizing */
    min-height: 40px; /* Minimum height */
    max-height: 200px; /* Maximum height */
}
</style>
""", unsafe_allow_html=True)

# Chat History (No Sidebar)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main Chat Area
with st.container():
    st.markdown("<div id='chat-area'>", unsafe_allow_html=True)  

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.markdown("</div>", unsafe_allow_html=True) 

# Input Box and Button at the Bottom (Docked and Centered)
with st.container():
    col1, col2 = st.columns([8, 1])  # Create two columns: one for input, one for button

    with col1:
        user_input = st.text_area("Your message", key="chat_input", height=40, max_chars=None)

    with col2:
        if st.button("Send", key="send_button") and user_input:
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

            # Clear the typing indicator
            message_placeholder.markdown(response) 

            # Clear the input box after sending the message
            st.session_state.chat_input = ""