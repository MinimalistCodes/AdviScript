import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
#switch_page


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
    st.info("Please select a page above.")
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
        st.info("Have a different API key? Enter it below.(Google Gemerative AI API Key)")
        # Chatbot settings form fields
        api_key = st.text_input("API Key", value=api_key)
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
            background-color: #f2f2f2;
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
# Dashbaord with cards gradient cards
st.markdown("### SalesTrek AI Sales Coach Dashboard")
st.markdown("Welcome to the SalesTrek AI Sales Coach Dashboard. You can ask any sales-related questions or request assistance with specific tasks.")
# Cards
col1, col2, col3 = st.columns(3)
# Card 1
with col1:
    st.markdown(
        """
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Script Generation</h5>
                <p class="card-text">Generate sales scripts for your sales calls and presentations.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
# Card 2
with col2:
    st.markdown(
        """
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Email Generation</h5>
                <p class="card-text">Generate email templates for your sales outreach campaigns.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
# Card 3
with col3:
    st.markdown(
        """
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">AI Sales Coach</h5>
                <p class="card-text">Ask any sales-related questions or request assistance with specific tasks.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
#----------------------------------
# Footer
#----------------------------------
st.markdown("---")  # Horizontal line
st.markdown("Made with :heart: by [SalesTrek](https://versiflow.cloud)")
st.markdown("© 2024 SalesTrek. All rights reserved.")
st.markdown("---")  # Horizontal line
#----------------------------------
  
