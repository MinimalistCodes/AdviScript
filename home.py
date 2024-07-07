import time
import streamlit as st
from dotenv import load_dotenv
import os, sys, json
from utils import ai_sales_coach, email_gen  # Import your functions from gen.py

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

# UI Layout
st.title("SalesTrek - Script Generator")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
st.markdown("<small>Chat history is saved in your browser's local storage.</small>", unsafe_allow_html=True)

# Custom CSS for Gemini-like styling with full-screen chat and docked input
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
  width: calc(100% - 30px); /* Account for padding */
  resize: vertical; /* Allow vertical resizing */
  min-height: 40px; /* Minimum height */
  max-height: 200px; /* Maximum height */
}
#chat-area { /* Container for chat messages */
  flex-grow: 1; /* Allow chat area to expand to fill available space */
  overflow-y: auto; /* Enable scrolling in the chat area */
}
</style>
""", unsafe_allow_html=True)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.container():  # Use container for styling
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User Input
if prompt := st.text_input("Your message"):
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display "Sales Coach is typing..."
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Sales Coach is typing...")

        # Simulate typing delay
        time.sleep(2)

        # Decide which function to call based on user input
        if "/script" in prompt.lower():
            response = ai_sales_coach(prompt)
        elif "/email" in prompt.lower():
            response = email_gen(prompt)
        else:
            response = "Please specify whether you need a sales script (/script) or an email template (/email)."

        # Update the placeholder with the AI response
        message_placeholder.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
