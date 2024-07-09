import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF


# Load environment va   riables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


st.set_page_config(
    page_title="SalesTrek - AI Sales Script Generator",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def save_chat_to_pdf(chat_history):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for message in chat_history:
        role = "User" if message["role"] == "user" else "Assistant"
        content = message["content"]
        pdf.multi_cell(0, 10, f"{role}: {content}")
        pdf.ln(10)

    pdf_file = "chat_history.pdf"
    pdf.output(pdf_file)
    return pdf_file

#load styles.css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    # clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
    st.markdown("---")  # Horizontal line
    #save to pdf button
    if st.button("Save Chat to PDF"):
        #use FPDF to save chat to pdf
        pdf_file = save_chat_to_pdf(st.session_state.messages)
        st.success(f"Chat history saved to {pdf_file}")
    st.markdown("---")  # Horizontal line
    # Chatbot settings
    st.markdown("### Chatbot Settings")
    st.markdown("Customize the chatbot settings.")
    # Chatbot settings form
    chatbot_settings = st.form("chatbot_settings")
    with chatbot_settings:
        # Chatbot settings form fields
        st.markdown("#### Chatbot Settings")
        st.info("Enter your Google API Key to enable the AI Sales Coach. (Get your API Key from the Google Cloud Console.)")
        # Chatbot settings form fields
        api_key = st.text_input("API Key", value=api_key)
        #if blank set to default
        if not api_key:
            api_key = os.getenv("GOOGLE_API_KEY")
        # Save button
        submit_button = st.form_submit_button("Save")
    # Save chatbot settings
    if submit_button:
        os.environ["GOOGLE_API_KEY"] = api_key
        st.success("Chatbot settings saved successfully.")

# UI Title
st.markdown("## SalesTrek - Your AI Sales Coach")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
st.markdown("---")  # Horizontal line
#----------------------------------
#Information Section

st.markdown("### SalesTrek AI Sales Coach")
st.markdown("SalesTrek AI Sales Coach is an AI-powered sales assistant that can help you with various sales tasks. You can ask any sales-related questions or request assistance with specific tasks.")
#Features in a table
st.markdown("### Features")
#table
st.markdown(
    """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th {
            background-color: #336699;
            color: #ffffff;
        }
        th, td {
            border: 1px solid black;
            text-align: left;
            color: #ffffff;
            padding: 8px;
        }
    </style>
    <table>
        <tr>
            <th>Feature</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>Script Generation</td>
            <td>Generate sales scripts for your sales calls and presentations.</td>
        </tr>
        <tr>
            <td>Email Generation</td>
            <td>Generate email templates for your sales outreach campaigns.</td>
        </tr>
        <tr>
            <td>AI Sales Coach</td>
            <td>Ask any sales-related questions or request assistance with specific tasks.</td>
        </tr>
    </table>
    """,
    unsafe_allow_html=True
)
st.markdown("---")  # Horizontal line 
#----------------------------------
# Dashbaord with cards gradient background color and icons
st.markdown("### SalesTrek AI Sales Coach Dashboard")
#cards
col1, col2, col3 = st.columns(3)
#card 1
with col1:
    st.markdown('<div class="card"><div class="card-body"><i class="fas fa-file-alt"></i><h3>Script Generation</h3><p>Generate sales scripts for your sales calls and presentations.</p></div></div>', unsafe_allow_html=True) 
#card 2
with col2:
    st.markdown('<div class="card"><div class="card-body"><i class="fas fa-envelope"></i><h3>Email Generation</h3><p>Generate email templates for your sales outreach campaigns.</p></div></div>', unsafe_allow_html=True)
#card 3
with col3:
    st.markdown('<div class="card"><div class="card-body"><i class="fas fa-user-tie"></i><h3>AI Sales Coach</h3><p>Ask any sales-related questions or request assistance with specific tasks.</p></div></div>', unsafe_allow_html=True)

st.markdown("---")  # Horizontal line


#----------------------------------
# Footer
#----------------------------------
st.markdown("---")  # Horizontal line
st.markdown("Made with :heart: by [SalesTrek](https://versiflow.cloud)")
st.markdown("© 2024 SalesTrek. All rights reserved.")
st.markdown("---")  # Horizontal line
#----------------------------------
  
