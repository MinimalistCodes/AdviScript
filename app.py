import streamlit as st
import pandas as pd
import numpy as np
import os
import google.generativeai as genai
from dotenv import load_dotenv
from IPython.display import Markdown
import textwrap

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-pro")

# Function to initialize the UI components
def main():
    st.set_page_config(page_title='Advi Script', layout='wide')
    st.title('Advi Script')
    st.markdown("An AI-powered chatbot designed to provide expert advice in the sales industry.")
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .chat-container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .user-message {
            margin: 10px 0;
            padding: 10px;
            background-color: #0077cc;
            color: white;
            border-radius: 5px;
        }
        .ai-message {
            margin: 10px 0;
            padding: 10px;
            background-color: #00cc77;
            color: white;
            border-radius: 5px;
            text-align: right;
        }
        </style>
        """, unsafe_allow_html=True)

    st.sidebar.markdown('## Settings')

    # Chat history list to store conversation
    chat_history = st.empty()

    # Input box for user messages
    user_input = st.text_input('You:', key='user_input')

    # Button to send user message
    if st.button('Send', key='send_button'):
        # Append user message to chat history
        append_message(f"You: {user_input}", 'user')

        # Placeholder for AI response
        ai_response = ai_chatbot(user_input)

        # Append AI response to chat history
        append_message(f"Advi Script: {ai_response}", 'ai')

# Function to append messages to chat history
def append_message(message, sender):
    if sender == 'user':
        chat_history.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
    elif sender == 'ai':
        chat_history.markdown(f'<div class="ai-message">{message}</div>', unsafe_allow_html=True)

# Function to simulate AI response (placeholder)
def ai_chatbot(message):
    prompt = cold_script(message)
    response = model.generate_text(prompt, max_length=100, temperature=0.5)
    return response

# Function to generate cold call script based on industry input
def cold_script(industry):
    return f"""
Please generate a cold call script tailored for a sales representative calling potential customers in the {industry} industry. Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""

if __name__ == '__main__':
    main()
