from datetime import datetime
import time

import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from PIL import Image
from pages import chat_with_coach, sales_script_generator, email_generator, summarizer, image_scan, settings

st.set_page_config(
    page_title="SalesTrek - AI Sales & Marketing Assistant",
    page_icon="🤖",
    layout="wide",
)

# Create an instance of the app 
app = st.create_app("SalesTrek - AI Sales & Marketing Assistant")
# Title of the main page
st.title("SalesTrek - AI Sales & Marketing Assistant")


# Add all your applications (pages) here
app.add_page("Chat with Coach", chat_with_coach.app)
app.add_page("Sales Script Generator", sales_script_generator.app)
app.add_page("Email Generator", email_generator.app)
app.add_page("Summarizer", summarizer.app)
app.add_page("Image Scan", image_scan.app)
app.add_page("Settings", settings.app)

# The main app
app.run()