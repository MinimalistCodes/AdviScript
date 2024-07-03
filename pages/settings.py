import streamlit as st
import runtimes as rt
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from PIL import Image
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF

#... rest of the chat functionality
st.header("Settings and Statistics")
st.write("This page displays settings and statistics for the app.") 
st.markdown("---") 
st.write("Settings")
st.write("Settings are not yet available.")
st.markdown("---")  
st.write("Statistics")
st.write(f"Total minutes used: {rt.total_time()}")
st.write(f"Scripts Generated: {rt.get_times_ran()}")
st.write(f"Last run: {rt.last_ran()}")