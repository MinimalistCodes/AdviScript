import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
from streamlit_tailwind import st_tailwind

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Google Generative AI
llm = GoogleGenerativeAI(model="gemini-pro")

# Define functions for different tasks
def generate_sales_script(prompt):
    response = llm(prompt)
    return response["text"]

def generate_email(prompt):
    response = llm(prompt)
    return response["text"]

def summarize_text(prompt):
    response = llm(prompt)
    return response["text"]

# Include Tailwind CSS
st.markdown("""
<head>
  <link href="https://unpkg.com/tailwindcss@^2.0/dist/tailwind.min.css" rel="stylesheet">
</head>
""", unsafe_allow_html=True)

# Main app function
def app():
    st.sidebar.title("SalesTrek AI Coach")
    st.title("Welcome to SalesTrek AI Coach")
    
    # Initialize session state for storing chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Display chat history
    for message in st.session_state.history:
        st.markdown(f"<div class='chat-message user-message'>{message['user']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-message bot-message'>{message['bot']}</div>", unsafe_allow_html=True)

    # Input box for user commands
    user_input = st.text_input("You:", key="user_input")

    if user_input:
        # Process the input
        if "generate script" in user_input.lower():
            prompt = user_input.replace("generate script", "").strip()
            result = generate_sales_script(prompt)
        elif "create email" in user_input.lower():
            prompt = user_input.replace("create email", "").strip()
            result = generate_email(prompt)
        elif "summarize" in user_input.lower():
            prompt = user_input.replace("summarize", "").strip()
            result = summarize_text(prompt)
        else:
            result = "Please enter a valid command."

        # Store the user input and bot response in session state
        st.session_state.history.append({"user": user_input, "bot": result})

        # Clear the input box
        st.session_state.user_input = ""

        # Refresh the page to display the new messages
        st.experimental_rerun()

# Run the app
if __name__ == "__main__":
    app()
