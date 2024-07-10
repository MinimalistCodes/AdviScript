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
    page_title="SalesTrek - Customer Management System",
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
st.markdown("## SalesTrek - Quick Customer Management.")
st.markdown("---")  # Horizontal line
#----------------------------------
#Simple CRM
crm = {}
#----------------------------------
# Chatbot
def chatbot(message):
    generative_ai = GoogleGenerativeAI(api_key)
    response = generative_ai.generate_text(message)
    return response

# Chatbot UI
with st.form("chat_form"):
    user_input = st.text_input("You:", key="user_input")
    st.session_state.messages = st.session_state.get("messages", [])
    if st.form_submit_button("Send"):
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            assistant_response = chatbot(user_input)
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        else:
            st.warning("Please enter a message.")
    st.markdown("---")  # Horizontal line
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        st.markdown(f"**{role.capitalize()}**: {content}")
        
#----------------------------------
# CRM
# CRM UI
st.sidebar.markdown("### CRM")
st.sidebar.markdown("Manage your customer relationships.")
# CRM form
crm_form = st.sidebar.form("crm_form")
with crm_form:
    st.sidebar.markdown("#### Add Customer")
    customer_name = st.sidebar.text_input("Name")
    customer_email = st.sidebar.text_input("Email")
    customer_phone = st.sidebar.text_input("Phone")
    submit_button = st.sidebar.form_submit_button("Add")
# Save customer
if submit_button:
    crm[customer_email] = {"name": customer_name, "phone": customer_phone}
    st.sidebar.success(f"Customer {customer_name} added successfully.")
# Display customers
if crm:
    st.sidebar.markdown("#### Customers")
    for email, customer in crm.items():
        st.sidebar.markdown(f"**{customer['name']}**")
        st.sidebar.markdown(f"Email: {email}")
        st.sidebar.markdown(f"Phone: {customer['phone']}")
        st.sidebar.markdown("---")
else:
    st.sidebar.info("No customers added yet.")
#----------------------------------
#----------------------------------

  
