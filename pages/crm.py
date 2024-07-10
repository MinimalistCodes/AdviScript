import streamlit as st
import pandas as pd

# Initialize CRM DataFrame
if "crm" not in st.session_state:
    st.session_state.crm = pd.DataFrame(columns=["Name", "Email", "Phone", "Company", "Status", "Priority"])

# Function to add or update customer
def add_or_update_customer(name, email, phone, company, status, priority):
    if email in st.session_state.crm["Email"].values:
        st.session_state.crm.loc[st.session_state.crm["Email"] == email, ["Name", "Phone", "Company", "Status", "Priority"]] = [name, phone, company, status, priority]
    else:
        new_customer = pd.DataFrame([[name, email, phone, company, status, priority]], columns=["Name", "Email", "Phone", "Company", "Status", "Priority"])
        st.session_state.crm = pd.concat([st.session_state.crm, new_customer], ignore_index=True)

# Function to delete customer
def delete_customer(email):
    st.session_state.crm = st.session_state.crm[st.session_state.crm["Email"] != email]

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
    add_or_update_customer(customer_name, customer_email, customer_phone, customer_company, customer_status, customer_priority)
    st.success(f"Customer {customer_name} added/updated successfully.")

# Search and Filter
st.markdown("### Search and Filter Customers")
search_term = st.text_input("Search by Name or Email")
filter_status = st.selectbox("Filter by Status", ["All", "Lead", "Customer"])

# Display all customers
st.markdown("### All Customers")
if filter_status == "All":
    filtered_customers = st.session_state.crm[(st.session_state.crm["Name"].str.contains(search_term, case=False)) | (st.session_state.crm["Email"].str.contains(search_term, case=False))]
else:
    filtered_customers = st.session_state.crm[(st.session_state.crm["Status"] == filter_status) & ((st.session_state.crm["Name"].str.contains(search_term, case=False)) | (st.session_state.crm["Email"].str.contains(search_term, case=False))]
st.table(filtered_customers)
