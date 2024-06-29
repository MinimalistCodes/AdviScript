import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown
import textwrap
import pathlib


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
def to_markdown(text):
  text = text.replace('•', '  *')
  text = text.replace('\n', '<br>')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function for AI chatbot interaction
def ai_chatbot(message):
    prompt = cold_script(message) # Assuming message here is the industry
    response = model.generate_content(prompt)  # Increased max_length
    to_markdown(response.text)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI and Chat Logic
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
        .message {
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
            max-width: 80%;
        }
        .user-message {
            background-color: #0077cc;
            color: white;
            align-self: flex-start;
        }
        .ai-message {
            background-color: #00cc77;
            color: white;
            align-self: flex-end;
        }
        .input-container {
            display: flex;
            align-items: center;
            margin-top: 20px;
        }
        .input-box {
            flex: 1;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .send-button {
            margin-left: 10px;
            padding: 10px 20px;
            border-radius: 5px;
            background-color: #0077cc;
            color: white;
            border: none;
            cursor: pointer;
        }
        </style>
""", unsafe_allow_html=True)

with st.form("input_form"):
    industry = st.selectbox(
        "Select Industry:",
        ["Technology", "Finance", "Healthcare", "Education", "Other"]
    )
    submitted = st.form_submit_button("Generate Script")
if submitted:
    script_type = cold_script(industry)
    response = ai_chatbot(script_type)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.text_input("You:", key="user_input")

# Send user message to chatbot
if st.button("Send"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = ai_chatbot(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat history
if st.button("Clear Chat"):
    st.session_state.messages = []

