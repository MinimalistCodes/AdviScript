import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
 from streamlit_extras.switch_page_button import switch_page

 
 st.set_page_config(
 page_title="AdviScript - AI Sales & Marketing Assistant",
 page_icon="🤖",
layout="wide",
initial_sidebar_state="collapsed",
)
# UI Layout

st.title("AdviScript - AI Sales & Marketing Assistant")


st.markdown(
    """
    <style>
        .reportview-container .main footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)


st.sidebar.title("Menu")
selected_page = st.sidebar.radio("Go to", ["Chat with Coach", "Sales Script Generator", "Email Generator", "Summarizer", "Image Scan", "Settings"])

if selected_page == "Chat with Coach":
    switch_page("Chat with Coach")  # Use switch_page for navigation
elif selected_page == "Sales Script Generator":
    switch_page("Sales Script Generator") 
    with st.expander("Instructions"):
        st.write("Type your prompt in the box below and click Send to generate your script.")
    # Load content from 1_sales_script_generator.py
elif selected_page == "Email Generator":
    st.subheader("Email Generator")
    with st.expander("Instructions"):
        st.write("Type your prompt in the box below and click Send to generate your email.")
    # Load content from 2_email_generator.py
elif selected_page == "Summarizer":
    st.subheader("Summarizer")
    with st.expander("Instructions"):
        st.write("Paste the text you want to summarize in the box below.")
    # Load content from 3_summarizer.py
elif selected_page == "Image Scan":
    st.subheader("Image Scan")
    with st.expander("Instructions"):
        st.write("Upload an image and let the AI analyze it.")
    # Load content from 4_image_scan.py
elif selected_page == "Settings":
    st.subheader("Settings")
    # Load content from 5_settings.py
