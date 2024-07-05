import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

from dotenv import load_dotenv
import io, os
import requests
import PIL.Image
from IPython.display import display
from IPython.display import Markdown
import textwrap


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))




load_dotenv()

#Load image fom file and display

st.title("SalesTrek - Image Scanner")
st.info("Please upload the image you would like to scan.")

image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if image:
    img = PIL.Image.open(image)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    llm = genai.GenerativeModel('gemini-pro-vision')
    response = llm.generate_content(img)
    
    st.write(to_markdown(response))
else:
    st.info("Please upload an image to begin.")
    
    