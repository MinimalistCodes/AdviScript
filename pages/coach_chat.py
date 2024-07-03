import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from PIL import Image

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def ai_sales_coach(user_input):
    # Preset Commands with Enhanced Replies
    preset_commands = {
        "/help": "Hi! I'm here to help you excel in sales. Whether you're a rep or a manager, I can assist with strategy, training, motivation, tools, and more. Just ask!",
        "/features": """I offer a wide range of features, including:
                      * Generating sales scripts and email templates
                      * Sales advice, objection handling, and closing techniques
                      * Prospecting, lead generation, and pipeline management strategies
                      * Guidance on presentations, demos, and building relationships
                      * Sales methodology explanations
                      * Sales training, coaching, and team building resources
                      * Sales performance analysis and tracking 
                      * Sales leadership and management advice
                      * ...and much more! Just ask away.""",
        "/about": "I'm an AI-powered sales coach built using Google's Gemini Pro model and LangChain.",
        "/clear": "Let's start fresh. What can I help you with today?",  
    }

    # Check for preset commands first
    if user_input in preset_commands:
        return preset_commands[user_input]
    else:
        # Enhanced Prompt for Sales Coach and Manager
        prompt = f"""
        You are an experienced sales leader and coach. You have in-depth knowledge of sales strategies, techniques, and best practices for both individual contributors and sales managers. You are skilled in providing guidance on:

        *   Sales methodologies (e.g., SPIN selling, Sandler, Challenger Sale)
        *   Effective communication and presentation skills
        *   Building rapport and trust with prospects and customers
        *   Handling objections and overcoming challenges
        *   Closing techniques and negotiation strategies
        *   Sales team management and leadership
        *   Motivating and coaching sales representatives
        *   Performance analysis and goal setting
        *   Recruiting, onboarding, and training new sales team members
        *   Developing and implementing sales strategies
        *   Analyzing market trends and identifying opportunities
        *   Utilizing CRM systems and other sales tools
        *   Building a positive and high-performing sales culture

        Please provide a comprehensive response to the following request from a sales professional:

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

st.markdown(
    """
    <style>
        .reportview-container .main footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)
    

# Display time and date
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.markdown(f"**Chat History:** {formatted_time}")  # Display time and date on the sidebar



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
