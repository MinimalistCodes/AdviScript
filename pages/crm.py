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
#----------------------------------
#Simple CRM
crm = {}
#----------------------------------
# Full Page CRM

st.title("Customer Relationship Management")
st.markdown("Manage your customer relationships.")

# Initialize CRM dictionary
if "crm" not in st.session_state:
    st.session_state.crm = {}

# Function to add or update customer
def add_or_update_customer(email, name, phone, company, status, priority):
    st.session_state.crm[email] = {
        "name": name,
        "phone": phone,
        "company": company,
        "status": status,
        "priority": priority
    }

# Function to delete customer
def delete_customer(email):
    if email in st.session_state.crm:
        del st.session_state.crm[email]

# CRM Form
crm_form = st.form("crm_form")
with crm_form:
    st.markdown("### Add or Update Customer")
    customer_name = st.text_input("Name")
    customer_email = st.text_input("Email")
    customer_phone = st.text_input("Phone")
    customer_company = st.text_input("Company")
    customer_status = st.selectbox("Status", ["Lead", "Customer"])
    customer_priority = st.slider("Priority", 1, 5)
    submit_button = st.form_submit_button("Add or Update")

# Save customer
if submit_button:
    add_or_update_customer(customer_email, customer_name, customer_phone, customer_company, customer_status, customer_priority)
    st.success(f"Customer {customer_name} added/updated successfully.")

# Search and Filter
st.markdown("### Search and Filter Customers")
search_term = st.text_input("Search by Name or Email")
filter_status = st.selectbox("Filter by Status", ["All", "Lead", "Customer"])

# Display customers
if st.session_state.crm:
    st.markdown("### Customers")
    for email, customer in st.session_state.crm.items():
        if (search_term.lower() in customer["name"].lower() or search_term.lower() in email.lower()) and (filter_status == "All" or filter_status == customer["status"]):
            st.markdown(f"**{customer['name']}**")
            st.markdown(f"Email: {email}")
            st.markdown(f"Phone: {customer['phone']}")
            st.markdown(f"Company: {customer['company']}")
            st.markdown(f"Status: {customer['status']}")
            st.markdown(f"Priority: {customer['priority']}")
            if st.button(f"Delete {customer['name']}", key=email):
                delete_customer(email)
                st.experimental_rerun()
            st.markdown("---")
else:
    st.info("No customers found.")


  
