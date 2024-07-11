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
    delete_button = st.form_submit_button("Delete")

# Save customer
if submit_button:
    add_or_update_customer(customer_name, customer_email, customer_phone, customer_company, customer_status, customer_priority)
    st.success(f"Customer {customer_name} added/updated successfully.")

# Filter customers
st.markdown("### Filter Customers")
status = st.selectbox("Status", ["All", "Lead", "Customer"])
priority = st.slider("Priority", 1, 5)

# Filter customers based on status and priority
filtered_customers = st.session_state.crm
if status != "All":
    filtered_customers = filtered_customers[filtered_customers["Status"] == status]
filtered_customers = filtered_customers[filtered_customers["Priority"] >= priority]

# Display customers table
st.markdown("### Customers")
st.table(filtered_customers)



#Delete Customer
if delete_button:
    delete_customer(customer_email)
    st.success(f"Customer {customer_name} deleted successfully.")
    

# Footer
st.markdown("---")
st.markdown("Made with :heart: by [SalesTrek](https://versiflow.cloud)")
st.markdown("© 2024 SalesTrek. All rights reserved.")
st.markdown("---")  # Horizontal line
#----------------------------------
