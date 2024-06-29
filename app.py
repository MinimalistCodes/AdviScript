import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import textwrap
import pandas as pd
from IPython.display import display
from IPython.display import Markdown
import textwrap
# Load environment variables from .env file (if you are using a .env file to store your API key)
load_dotenv()

# Initialize Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-pro")
# Function to generate the cold call script
def cold_script(industry):
    return f"""
Please generate a cold call script tailored for a sales representative calling potential customers in the {industry} industry. Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""
#use css to style.css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")



# Function to format text as Markdown with indentation
def to_markdown(text):
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def display_markdown(text):
    display(to_markdown(text))
    

# Function for AI chatbot interaction
def ai_chatbot(txt):
    prompt = cold_script(txt)
    response = model.generate_content(cold_script(txt))
    st.write(response.text)
    return response.text

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI and Chat Logic
st.set_page_config(page_title='Advi Script', layout='wide')
st.title('Advi Script')
st.markdown("An AI-powered chatbot designed to provide expert advice in the sales industry.")

# Sidebar to display conversation history
         
def display_old_conversation(i):
    conversation = st.session_state.messages[i:]
    for message in conversation:
        if message["role"] == "user":
            display_markdown(f"**User:** {message['content']}")
        else:
            display_markdown(f"**Assistant:** {message['content']}")
    st.session_state.current_conversation = i
    st.session_state.showing_conversation = True
    st.session_state.showing_history = False

# Form for selecting industry and sending user message to chatbot
form = st.form("input_form")
form_choice = form.selectbox(
    "Select Industry:",
    ["Technology", "Finance", "Healthcare", "Education", "Sales", "Other"]
)

# Handling selection of "Other" industry
if form.form_submit_button("Choose Industry"):
    if form_choice == "Other":
        other_industry = form.text_input("Please specify the industry:")
        st.write(f"Generating a cold call script for the {other_industry} industry...")
        st.session_state.messages.append({"role": "user", "content": other_industry})
        #if other show text input
    else:
        st.write(f"Generating a cold call script for the {form_choice} industry...")
        st.session_state.messages.append({"role": "user", "content": form_choice})
        response = ai_chatbot(form_choice)
    # Display the assistant's response if button is clicked
    if st.button("Generate Script"):
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.session_state.showing_history = False
        st.session_state.showing_conversation = True
    
with st.sidebar:
    sidebar_title = st.markdown("Conversation History")
    if "messages" in st.session_state:
        for i, message in enumerate(st.session_state.messages):
            if st.button(f"Message {i + 1}"):
                display_old_conversation(i)
    if "showing_conversation" in st.session_state:
        if st.button("Back to Conversation History"):
            st.session_state.showing_conversation = False
            st.session_state.showing_history = True
    if "showing_history" in st.session_state:
        if st.button("Back to Industry Selection"):
            st.session_state.showing_history = False
            st.session_state.showing_conversation = False
            st.session_state.messages = []
            
            
# Display the conversation history
if st.session_state.showing_conversation:
    display_old_conversation(st.session_state.current_conversation)


    