import streamlit as st
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
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


st.sidebar.success("Select a page above.")

st.set_page_config(
    page_title="SalesTrek - Your multi-tool for sales and marketing!",
    page_icon="📈"
)

st.title("Main Page")
st.write("Welcome to SalesTrek! Your multi-tool for sales and marketing!")
st.markdown("---")
st.header("User Statistics")
st.write(f"Total minutes used: {rt.total_time()}")
st.write(f"Scripts Generated: {rt.get_times_ran()}")
st.write(f"Last run: {rt.last_ran()}")