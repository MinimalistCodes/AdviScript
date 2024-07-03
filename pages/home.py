from datetime import datetime
import time

import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from st_paywall import Paywall


# Home Page Content
def app():
    st.markdown("<h1 style='text-align: center;'>🚀 Welcome to SalesTrek</h1>", unsafe_allow_html=True)
    # You can add your about section content here
    st.write("""
    SalesTrek is your AI-powered sales and marketing assistant designed to help you succeed in the competitive world of sales. Whether you're an experienced sales professional or new to the field, SalesTrek has the tools and guidance you need to achieve your goals.
    """)
    
    st.markdown("### ✨Features")
    st.write("""
    SalesTrek offers a range of features, including:
    - AI Sales Coach: Get expert advice and guidance on sales strategies, objection handling, and more.
    - Sales Script Generator: Generate custom sales scripts and email templates tailored to your needs.
    - Email Generator: Create engaging and effective email templates for your sales campaigns.
    - Summarizer: Summarize long texts or articles quickly and efficiently.
    - Image Scan: Analyze images and extract text for further processing.
    - Settings: Customize your SalesTrek experience with personalized settings.
    """)
    
    st.markdown("### 🤔 How to Use")
    st.write("""
    To get started, simply select one of the features from the sidebar menu. 
    Each feature is designed to help you improve your sales and marketing skills, generate high-quality content, and optimize your workflow.
    """)
app()        