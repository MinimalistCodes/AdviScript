import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from streamlit_navigation_bar import st_navbar


# Load environment va   riables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


st.set_page_config(
    page_title="SalesTrek - AI Sales Script Generator",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)

#load styles.css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


page = st_navbar(["Script Generation", "Email Generation", "AI Sales Coach"])
if page == "main":
    st.switch_page("main.py")
if page == "script":
    st.switch_page("script.py")
if page == "Email":
    st.switch_page("email.py")
if page == "Coach":
    st.switch_page("coach.py")


# UI Title
st.markdown("## SalesTrek - Your AI Sales Coach")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
st.markdown("---")  # Horizontal line
#----------------------------------
#Information Section

st.markdown("### SalesTrek AI Sales Coach")
st.markdown("SalesTrek AI Sales Coach is an AI-powered sales assistant that can help you with various sales tasks. You can ask any sales-related questions or request assistance with specific tasks.")
#Features in a table
st.markdown("### Features")
#table
st.markdown(
    """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th {
            background-color: #f2f2f2;
        }
        th, td {
            border: 1px solid black;
            text-align: left;
            padding: 8px;
        }
    </style>
    <table>
        <tr>
            <th>Feature</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>Script Generation</td>
            <td>Generate sales scripts for your sales calls and presentations.</td>
        </tr>
        <tr>
            <td>Email Generation</td>
            <td>Generate email templates for your sales outreach campaigns.</td>
        </tr>
        <tr>
            <td>AI Sales Coach</td>
            <td>Ask any sales-related questions or request assistance with specific tasks.</td>
        </tr>
    </table>
    """,
    unsafe_allow_html=True
)
st.markdown("---")  # Horizontal line 
#----------------------------------
# Dashbaord with cards
#----------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### Sales Script Generation")
    st.markdown("Generate sales scripts for your sales calls and presentations.")
    st.markdown("![Sales Script Generation](https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif)")
with col2:
    st.markdown("### Email Generation")
    st.markdown("Generate email templates for your sales outreach campaigns.")
    st.markdown("![Email Generation](https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif)")
with col3:
    st.markdown("### AI Sales Coach")
    st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
    st.markdown("![AI Sales Coach](https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif)")
#----------------------------------
# Footer
#----------------------------------
st.markdown("---")  # Horizontal line
st.markdown("Made with :heart: by [SalesTrek](https://versiflow.cloud)")
st.markdown("© 2024 SalesTrek. All rights reserved.")
st.markdown("---")  # Horizontal line
#----------------------------------
  
