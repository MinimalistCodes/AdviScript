import streamlit as st

# Home Page Content
def app():
    st.markdown("<h1 style='text-align: center;'>Welcome to SalesTrek</h1>", unsafe_allow_html=True)
    # You can add your about section content here
    st.write("""
    SalesTrek is your AI-powered sales and marketing assistant designed to help you succeed in the competitive world of sales. Whether you're an experienced sales professional or new to the field, SalesTrek has the tools and guidance you need to achieve your goals.
    """)
    
