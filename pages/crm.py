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

# Initialize the CRM dictionary
if 'crm' not in st.session_state:
    st.session_state.crm = {}

def add_customer():
    crm_form = st.form("crm_form")
    with crm_form:
        st.markdown("### Add Customer")
        customer_name = st.text_input("Name")
        customer_email = st.text_input("Email")
        customer_phone = st.text_input("Phone")
        customer_company = st.text_input("Company")
        customer_status = st.selectbox("Status", ["Lead", "Customer"])
        customer_priority = st.slider("Priority", 1, 5)
        submit_button = st.form_submit_button("Add")

    # Save customer
    if submit_button:
        st.session_state.crm[customer_email] = {
            "name": customer_name,
            "phone": customer_phone,
            "company": customer_company,
            "status": customer_status,
            "priority": customer_priority,
        }
        st.success(f"Customer {customer_name} added successfully.")

def edit_customer(email):
    customer = st.session_state.crm[email]
    crm_form = st.form(f"edit_form_{email}")
    with crm_form:
        st.markdown(f"### Edit Customer: {customer['name']}")
        customer_name = st.text_input("Name", value=customer['name'])
        customer_phone = st.text_input("Phone", value=customer['phone'])
        customer_company = st.text_input("Company", value=customer['company'])
        customer_status = st.selectbox("Status", ["Lead", "Customer"], index=["Lead", "Customer"].index(customer['status']))
        customer_priority = st.slider("Priority", 1, 5, value=customer['priority'])
        submit_button = st.form_submit_button("Update")

    # Update customer
    if submit_button:
        st.session_state.crm[email] = {
            "name": customer_name,
            "phone": customer_phone,
            "company": customer_company,
            "status": customer_status,
            "priority": customer_priority,
        }
        st.success(f"Customer {customer_name} updated successfully.")

def display_customers():
    filter_status = st.selectbox("Filter by Status", ["All", "Lead", "Customer"])
    search_query = st.text_input("Search by Name or Email")

    filtered_customers = {
        email: customer for email, customer in st.session_state.crm.items()
        if (filter_status == "All" or customer['status'] == filter_status) and
           (search_query.lower() in customer['name'].lower() or search_query.lower() in email.lower())
    }

    if filtered_customers:
        st.markdown("### Customers")
        for email, customer in filtered_customers.items():
            st.markdown(f"**{customer['name']}**")
            st.markdown(f"Email: {email}")
            st.markdown(f"Phone: {customer['phone']}")
            st.markdown(f"Company: {customer['company']}")
            st.markdown(f"Status: {customer['status']}")
            st.markdown(f"Priority: {customer['priority']}")
            edit_button = st.button("Edit", key=f"edit_{email}")
            delete_button = st.button("Delete", key=f"delete_{email}")
            if edit_button:
                edit_customer(email)
            st.markdown("---")
    else:
        st.info("No customers found.")

# Display the form to add a new customer
add_customer()

# Display customers with options to edit and delete
display_customers()
        
#----------------------------------



  
