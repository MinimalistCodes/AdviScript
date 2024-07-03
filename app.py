import streamlit as st
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from PIL import Image

st.set_page_config(
    page_title="SalesTrek - Your multi-tool for sales and marketing!",
    page_icon="📈"
)

st.title("Main Page")
st.sidebar.success("Select a page above.")