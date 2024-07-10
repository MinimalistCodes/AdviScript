import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF


# Load environment va   riables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def ai_sales_coach(user_input):
      llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
      return llm.invoke(user_input)


st.set_page_config(
    page_title="SalesTrek - Customer Management System",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)


#load styles.css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#----------------------------------
#Simple CRM
crm = {}
#----------------------------------
# CRM
# CRM UI
with st.sidebar:
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
# Chatbot
# Chatbot UI
st.markdown("### Chatbot")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
# Chatbot form
chat_form = st.form("chat_form")
with chat_form:
    user_input = st.text_input("You")
    submit_button = st.form_submit_button("Send")
# Save chat
if "messages" not in st.session_state:
    st.session_state.messages = []
if submit_button:
    st.session_state.messages.append({"role": "user", "content": user_input})
    assistant_response = ai_sales_coach(user_input)
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
# Display chat
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    if role == "user":
        st.markdown(f"**You:** {content}")
    else:
        st.markdown(f"**Assistant:** {content}")
#----------------------------------


  
