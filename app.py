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

# Function to format text as Markdown with indentation
def to_markdown(text):
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function for AI chatbot interaction
def ai_chatbot(txt):
    prompt = cold_script(txt)
    response = model.generate_content(cold_script(txt))
    st.write(response.text)
    
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
def show_old_conversation(index):
    st.session_state.current_conversation = index
    st.session_state.showing_history = False
    st.session_state.showing_conversation = True

# Display old conversations in sidebar with links
for index, message in enumerate(st.session_state.messages):
    if message["role"] == "assistant" and f'Advi Script {index}' not in st.session_state:
        st.session_state[f'Advi Script {index}'] = st.sidebar.button(f'Advi Script {index}')
    elif message["role"] == "user" and f'You {index}' not in st.session_state:
        st.session_state[f'You {index}'] = st.sidebar.button(f'You {index}')

    if st.session_state.get(f'Advi Script {index}') or st.session_state.get(f'You {index}'):
        show_old_conversation(index)

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
        st.session_state.messages.append({"role": "assistant", "content": response})
        #Get Script Button  
        if st.button("Get Script"):
            #export the script to a text file
            with open("cold_call_script.txt", "w") as file:
                file.write(response.text)
            #clear the chat
            st.session_state.messages = []
            st.write("The cold call script has been exported to cold_call_script.txt")
            if os.path.exists("cold_call_script.txt"):
                st.download_button(label="Download Script", data="cold_call_script.txt", file_name="cold_call_script.txt", mime="text/plain")
            else:
                st.write("Error: File not found")

    st.session_state.messages.append({"role": "assistant", "content": response})


# Buttons for exporting and clearing chat
col1, col2 = st.columns(2)

with col1:
    if st.button("Export Script"):
        #export the script to a text file
        with open("cold_call_script.txt", "w") as file:
            file.write(response.text)
        #clear the chat
        st.session_state.messages = []
        st.write("The cold call script has been exported to cold_call_script.txt")
        if os.path.exists("cold_call_script.txt"):
            st.download_button(label="Download Script", data="cold_call_script.txt", file_name="cold_call_script.txt", mime="text/plain")
        else:
            st.write("Error: File not found")

with col2:
    if st.button("Clear Chat"):
        st.session_state.messages = []