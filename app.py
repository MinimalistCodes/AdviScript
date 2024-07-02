import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from g4f.client import Client


# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

# Available LLM Options
LLM_OPTIONS = {
    "Google Gemini Pro": (GoogleGenerativeAI, {"model": "gemini-pro", "google_api_key": api_key}),
    "GPT4Free - you.com": (Provider, {"name": "you.com"}),
    "GPT4Free - phind.com": (Provider, {"name": "phind.com"}),
    "GPT4Free - theb.ai": (Provider, {"name": "theb.ai"}),
    # Add more GPT4Free providers if needed
}


# Get LLM Response
def get_llm_response(user_input, llm_class, llm_kwargs):
    llm = llm_class(**llm_kwargs) 
    try:
        if llm_class == GoogleGenerativeAI:
            preset_commands = {
                "/help": "Hi there! I'm your AI sales coach. How can I help you?",
                "/features": "I can help with generating scripts, handling objections, sales strategies, and more. Just ask!",
                "/about": "I'm built using Google's Gemini Pro model and LangChain framework.",
                "/clear": "Sure! Let's start fresh. How can I assist you today?", # Clear chat history    
                }
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
            return llm.invoke(prompt)
     else:  # GPT4Free
            messages = [{"role": "user", "content": user_input}]
            response = llm.create(model="gpt-3.5-turbo", messages=messages)
            return response["choices"][0]["message"]["content"]  # Extract the response text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, I couldn't process your request at this time. Please try again later."

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, I couldn't process your request at this time. Please try again later."

# UI Layout
st.title("Advi Script - Your AI Sales Coach")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
st.markdown("<small>Chat history is saved in your browser's local storage.</small>", unsafe_allow_html=True)

# Sidebar (LLM Selection and Theme Options)
with st.sidebar:
    st.subheader("LLM Selection")
    selected_llm = st.selectbox("Choose your LLM:", list(LLM_OPTIONS.keys()))
    st.session_state.selected_llm = selected_llm
    
    # Theme Options
    st.subheader("Theme Options")
    theme = st.selectbox("Select a theme", ["Light", "Dark", "Custom"])
    
    # Apply theme based on selection
    if theme == "Light":
        st.markdown(
            """
            <style>
            body {
                background-color: #F0F0F0;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    elif theme == "Dark":
        st.markdown(
            """
            <style>
            body {
                background-color: #1E1E1E;
                color: #FFFFFF;
            }
            .chat-message {
                background-color: #2E2E2E;
                color: #FFFFFF;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:  # Custom theme
        custom_css = st.text_area("Custom CSS")
        st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Load chat history from local storage
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
    llm_class, llm_kwargs = LLM_OPTIONS[st.session_state.selected_llm]
    response = get_llm_response(user_input, llm_class, llm_kwargs)
    message_placeholder.markdown(response)  # Update the placeholder
    st.session_state.messages.append({"role": "assistant", "content": response})

col1, col2 = st.columns(2)  # Create two columns for the buttons


st.session_state.stored_messages = json.dumps(st.session_state.messages)
