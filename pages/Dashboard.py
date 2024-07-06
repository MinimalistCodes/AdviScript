import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="SalesTrek Dashboard",
    page_icon=":rocket:",
    layout="wide",
)

# Sidebar
st.sidebar.title("SalesTrek")
st.sidebar.subheader("Navigation")

# Page navigation buttons
if st.sidebar.button("Script Generator"):
    switch_page("Script Generator")

if st.sidebar.button("Email Generator"):
    switch_page("Email Generator")

if st.sidebar.button("AI Sales Coach"):
    switch_page("AI Sales Coach")

if st.sidebar.button("Settings"):
    switch_page("Settings")

# Main dashboard content
st.title("Welcome to SalesTrek Dashboard")

st.write(
    """
    This is your main dashboard. Use the sidebar to navigate to different tools.
    """
)

# Dashboard widgets and data visualization
st.header("Sales Summary")
st.write("Here you can add widgets, charts, and other dashboard components.")

# Example of data visualization
st.subheader("Monthly Sales")
sales_data = {
    "January": 120,
    "February": 150,
    "March": 200,
    "April": 300,
    "May": 500,
}
months = list(sales_data.keys())
sales = list(sales_data.values())

st.bar_chart(sales_data)

st.subheader("Sales Funnel")
funnel_data = {
    "Leads": 1000,
    "Qualified Leads": 600,
    "Proposals": 400,
    "Closed Deals": 250,
}

funnel_fig = {
    'Leads': [1000, 600, 400, 250],
    'Qualified Leads': [600, 400, 250, 0],
    'Proposals': [400, 250, 0, 0],
    'Closed Deals': [250, 0, 0, 0]
}

st.bar_chart(funnel_fig)

# Additional content and layout adjustments
st.write("Add more content and adjust the layout as needed.")

# Run the app
if __name__ == "__main__":
    app()
