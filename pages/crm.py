import streamlit as st
import pandas as pd

# Initialize or load CRM DataFrame
@st.cache(allow_output_mutation=True)
def load_data():
    return pd.DataFrame(columns=["Name", "Email", "Phone", "Company", "Status", "Priority"])

crm = load_data()

# Function to add or update customer
def add_or_update_customer(name, email, phone, company, status, priority):
    global crm
    if email in crm["Email"].values:
        crm.loc[crm["Email"] == email, ["Name", "Phone", "Company", "Status", "Priority"]] = [name, phone, company, status, priority]
    else:
        new_customer = pd.DataFrame([[name, email, phone, company, status, priority]], columns=["Name", "Email", "Phone", "Company", "Status", "Priority"])
        crm = pd.concat([crm, new_customer], ignore_index=True)
    st.experimental_rerun()

# Function to delete customer
def delete_customer(email):
    global crm
    crm = crm[crm["Email"] != email]
    st.experimental_rerun()

# Main Streamlit app
def main():
    st.title("Mini CRM")
    
    # CRM Form
    st.sidebar.header("Add or Update Customer")
    customer_name = st.sidebar.text_input("Name")
    customer_email = st.sidebar.text_input("Email")
    customer_phone = st.sidebar.text_input("Phone")
    customer_company = st.sidebar.text_input("Company")
    customer_status = st.sidebar.selectbox("Status", ["Lead", "Customer"])
    customer_priority = st.sidebar.slider("Priority", 1, 5, 3)
    submit_button = st.sidebar.button("Add or Update")

    if submit_button:
        add_or_update_customer(customer_name, customer_email, customer_phone, customer_company, customer_status, customer_priority)
        st.sidebar.success(f"Customer {customer_name} added/updated successfully.")
    
    # Display customers
    st.header("Customers")
    if not crm.empty:
        st.dataframe(crm)
        for index, customer in crm.iterrows():
            if st.button(f"Delete {customer['Name']}"):
                delete_customer(customer['Email'])
    else:
        st.info("No customers found.")

if __name__ == "__main__":
    main()
