import streamlit as st
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import runtimes as rt
from extra_streamlit_components import TabBar




#get todays date and save it
import datetime
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d %H:%M:%S")
rt.todaysDate = date
#set the mins and hours used to 0
rt.mins_used = 0
rt.hours_used = 0

# Define your tab data
tab_labels = ["Home", "Image Scanner", "Script Generator", "About"]
tab_icons = ["🏠", "📷", "📝", "ℹ️"] # Example icons, replace with your own
tab_data = [
    {"id": "home", "label": tab_labels[0], "icon": tab_icons[0]},
    {"id": "image_scanner", "label": tab_labels[1], "icon": tab_icons[1]},
    {"id": "script_generator", "label": tab_labels[2], "icon": tab_icons[2]},
    {"id": "about", "label": tab_labels[3], "icon": tab_icons[3]},
]

# Create the tab bar
tab_bar = TabBar(data=tab_data, key="main_tab_bar")

# Display content based on selected tab
if tab_bar == "home":
    st.write("Welcome to the home page!")  # Your home page content
elif tab_bar == "image_scanner":
    image_scan()  
elif tab_bar == "script_generator":
    script_gen()  
elif tab_bar == "about":
    st.write("About this app...")  # Your about page content