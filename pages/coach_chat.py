import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import time
import json
import os
from fpdf import FPDF
import datetime
import openai

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Please set your OPENAI_API_KEY in the .env file.")
    st.stop()

# Initialize OpenAI model with session state for persistence
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = OpenAI(temperature=0.7, openai_api_key=api_key)

# Initialize conversation chain with session state for persistence
if "chain" not in st.session_state:
    st.session_state.chain = ConversationChain(llm=st.session_state["openai_model"])

# Function to generate responses from the AI Sales Coach
def ai_sales_coach(user_input):
    prompt = f"""You are an expert sales coach employed at [Your Company Name]. You have a deep understanding of our company's products, services, target market, and sales strategies. You are also well-versed in general sales methodologies, techniques, and best practices.

    Your goal is to help [Your Company Name]'s sales team achieve their highest potential. You can provide guidance on various aspects of sales, including:

    *   Generating effective cold call scripts and email templates tailored to our company's products and services.
    *   Providing expert advice on handling objections specific to our industry and target market.
    *   Offering proven tips for closing deals based on our sales process.
    *   Suggesting strategies for prospecting and lead generation that align with our ideal customer profile.
    *   Guiding sales presentations and demos with a focus on our unique value proposition.
    *   Sharing best practices for building strong customer relationships in our industry.
    *   Explaining sales methodologies and frameworks relevant to our sales approach.
    *   Assisting with sales training and coaching sessions for our team.
    *   Fostering team building and motivation within our sales department.
    *   Offering advice on sales management and leadership for team leaders.
    *   Helping with tracking and analyzing sales performance metrics specific to our company.
    *   Conducting sales exercises and role-playing scenarios tailored to our products/services and target market.
    *   Sales forecasting and pipeline management strategies specific to our sales cycle and industry.
    *   Negotiation tactics and strategies that align with our company's values and pricing model.
    *   Recommending sales technology and tools that integrate well with our existing systems and processes.
    *   Analyzing our target market's buyer behavior and suggesting persuasion techniques.
    *   Ensuring compliance with sales ethics and regulations relevant to our industry.

    Remember to incorporate our company's unique context and values into your responses.  Please provide a comprehensive response to the following request:

    {user_input}"""

    response = st.session_state.chain.run(prompt)
    return response

# UI Layout
st.title("SalesTrek - Script Generator")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
st.markdown("<small>Chat history is saved in your browser's local storage.</small>", unsafe_allow_html=True)

# Custom CSS for Gemini-like styling
# ... [Your existing CSS code]

# Display time and date
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.markdown(f"**Chat History:** {formatted_time}")  # Display time and date on the sidebar

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


# Main Chat Area
with st.container():
    st.markdown("<div id='chat-area'>", unsafe_allow_html=True) 

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.markdown("</div>", unsafe_allow_html=True)  

# Input Box at the Bottom (Docked and Centered)
with st.container():
    user_input = st.text_area("Your message", key="chat_input", height=40, on_change=None)
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Display "Sales Coach is thinking..." message
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.status("Thinking...", expanded=True) as status:
                st.write("Combing over resources...")
                time.sleep(2)
                st.write("Script finished")
                time.sleep(1)
                st.write("Sending script...")
                time.sleep(1)  
                status.update(label="Crafting complete!", state="complete", expanded=False)  
                message_placeholder.markdown("Sales Coach is typing...")
                response = ai_sales_coach(prompt)
                message_placeholder.markdown(response) 
                st.session_state.messages.append({"role": "assistant", "content": response})

        # Clear the input box after sending the message
        st.session_state.chat_input = ""

        # Save chat history to local storage
        st.session_state.stored_messages = json.dumps(st.session_state.messages)


# Buttons in a Row (under the input box)
with st.container():
    st.markdown("<div id='button-container'>", unsafe_allow_html=True)  
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear History"):
            st.session_state.messages = []
            st.session_state.pop("stored_messages", None)
            st.experimental_rerun()

    with col2:
        if st.button("Export Chat to PDF"):
            # ... PDF export code (same as before) ...
    st.markdown("</div>", unsafe_allow_html=True)  # Close button container
