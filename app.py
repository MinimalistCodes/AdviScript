import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from IPython.display import Markdown
import textwrap
import pandas as pd

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

# Function to format text as Markdown with indentation
def to_markdown(text):
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function for AI chatbot interaction
def ai_chatbot(message):
    prompt = cold_script(message)  # Assuming message here is the industry
    prompt = prompt.replace("\n", "<br>").replace(" ", "&nbsp;")
    prompt = f"<p>{prompt}</p>"
    prompt = prompt.replace('•', '  *')
    prompt = prompt.replace("*", "<b>").replace("*", "</b>")
    response = model.generate_content(prompt)
    st.write(response)



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI and Chat Logic
st.set_page_config(page_title='Advi Script', layout='wide')
st.title('Advi Script')
st.markdown("An AI-powered chatbot designed to provide expert advice in the sales industry.")

# Sidebar to display conversation history
st.sidebar.title("Conversation History")


# Function to handle clicking on old conversations
def show_old_conversation(message):
    st.session_state.current_conversation = message
    st.session_state.showing_history = False
    st.session_state.showing_conversation = True

# Display old conversations in sidebar with links
for index, message in enumerate(st.session_state.messages):
    if message["role"] == "assistant":
        if st.sidebar.button(f'Advi Script {index}'):
            show_old_conversation(message)
    elif message["role"] == "user":
        if st.sidebar.button(f'You {index}'):
            show_old_conversation(message)

# User input for sending direct messages to the chatbot
user_input = st.text_input("You:", key="user_input")

# Form for selecting industry and sending user message to chatbot
form = st.form("input_form")
form_choice = form.selectbox(
    "Select Industry:",
    ["Technology", "Finance", "Healthcare", "Education", "Sales", "Other"]
)

# Handling selection of "Other" industry
if form_choice == "Other":
    other_industry = form.text_input("Please specify the industry:")
    if form.form_submit_button("Send"):
        st.write(f"Generating a cold call script for the {other_industry} industry...")
        st.session_state.messages.append({"role": "user", "content": other_industry})
        response = ai_chatbot(other_industry)
        st.session_state.messages.append({"role": "assistant", "content": response})
else:
    if form.form_submit_button("Send"):
        st.write(f"Generating a cold call script for the {form_choice} industry...")
        st.session_state.messages.append({"role": "user", "content": form_choice})
        response = ai_chatbot(form_choice)
        st.session_state.messages.append({"role": "assistant", "content": response})

# New Convo button to clear chat history and save to Pandas DataFrame
if st.button("New Convo"):
    # Save current conversation to Pandas DataFrame
    df = pd.DataFrame(st.session_state.messages)
    df.to_csv("conversation_history.csv", index=False)
    
    # Clear chat history
    st.session_state.messages = []

# Clear chat history button
if st.button("Clear Chat"):
    st.session_state.messages = []

# Viewing previous conversation

