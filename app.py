import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.dataframe_explorer import dataframe_explorer

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def ai_sales_coach(user_input):
    preset_commands = {
        "/help": "Hi there! I'm your AI sales coach. How can I help you?",
        "/features": "I can help with generating scripts, handling objections, sales strategies, and more. Just ask!",
        "/about": "I'm built using Google's Gemini Pro model and LangChain framework.",
        "/clear": "Sure! Let's start fresh. How can I assist you today?", # Clear chat history
        
    }

    # Check for preset commands first
    if user_input in preset_commands:
        return preset_commands[user_input]
    else:
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

        try:
            llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
            return llm.invoke(prompt)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return "Sorry, I couldn't process your request at this time. Please try again later."

# UI Layout
st.title("Advi Script - Your AI Sales Coach")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
st.markdown("<small>Chat history is saved in your browser's local storage.</small>", unsafe_allow_html=True)
# JavaScript Code for Theme Switching

st.sidebar.title("Theme")
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if st.button("Toggle Theme"):
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Dynamic CSS based on theme
st.markdown(
    f"""
    <style>
        body {{
            background-color: {'#262730' if st.session_state.theme == "dark" else '#ffffff'};
            color: {'#ffffff' if st.session_state.theme == "dark" else '#262730'};
        }}
        .chat-message {{
            background-color: {'#40414F' if st.session_state.theme == "dark" else '#F0F0F0'};
            color: {'#ffffff' if st.session_state.theme == "dark" else '#333333'};
        }}
        .user-message {{
            background-color: {'#545569' if st.session_state.theme == "dark" else '#E2F0FF'}; 
        }}
        #chat-input-container {{
            background-color: {'#333444' if st.session_state.theme == "dark" else '#FFFFFF'};
        }}
        #chat-input {{
            color: {'#ffffff' if st.session_state.theme == "dark" else '#262730'};
        }}
    </style>
    """,
    unsafe_allow_html=True,



# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

    try:
        stored_messages = st.session_state.get("stored_messages", None)
        if stored_messages:
            st.session_state.messages = json.loads(stored_messages)
    except json.JSONDecodeError:
        st.error("Error loading chat history from local storage.")


with st.container():  # Use container for styling
    for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
            
   
# User Input
if prompt := st.chat_input("Your message"):
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display "Sales Coach is typing..."
    with st.chat_message("assistant"):
        message_placeholder = st.empty() 
        message_placeholder.markdown("Sales Coach is typing...")

    # Get and append AI response (with a delay to simulate typing)
    time.sleep(1)  # Adjust the delay as needed
    response = ai_sales_coach(prompt)
    message_placeholder.markdown(response)  # Update the placeholder
    st.session_state.messages.append({"role": "assistant", "content": response})

col1, col2 = st.columns(2)  # Create two columns for the buttons


st.session_state.stored_messages = json.dumps(st.session_state.messages)
