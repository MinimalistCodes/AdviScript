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
    flex-direction: column;
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
#chat-area {
    flex-grow: 1; /* Allow chat area to expand to fill available space */
    overflow-y: auto; /* Enable scrolling in the chat area */
}
#chat-input-container {
    background-color: #FFFFFF; /* White background for input area */
    padding: 15px;
}
#chat-input {
    width: calc(100% - 30px); /* Account for padding */
    resize: vertical;
    min-height: 40px; 
    max-height: 200px; 
}
</style>
""", unsafe_allow_html=True)

# Chat History and Input (Reversed Order)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input Box at the Bottom (Docked and Centered)
with st.container():  
    with st.form(key="chat_form"):
        user_input = st.text_area("Your message", key="chat_input", height=40, max_chars=None)
        submitted = st.form_submit_button("Send")
        if submitted:
            if user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                

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

                # Clear the input box after sending the message
                st.session_state.chat_input = ""


# Main Chat Area
with st.container():
    st.markdown("<div id='chat-area'>", unsafe_allow_html=True) 
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.markdown("</div>", unsafe_allow_html=True) 