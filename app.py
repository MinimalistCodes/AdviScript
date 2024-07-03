import streamlit as st
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import runtimes as rt

#get todays date and save it
import datetime
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d %H:%M:%S")
rt.todaysDate = date
#set the mins and hours used to 0
rt.mins_used = 0
rt.hours_used = 0



st.set_page_config(
    page_title="SalesTrek - Your multi-tool for sales and marketing!",
    page_icon="📈"
)

st.title("Main Page")
st.write("Welcome to SalesTrek! Your multi-tool for sales and marketing!")
st.write("This app is powered by Google's Gemini Pro model and LangChain framework.")
st.write("Please select a tool from the sidebar to get started.")