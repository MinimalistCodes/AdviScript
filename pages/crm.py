import streamlit as st

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
