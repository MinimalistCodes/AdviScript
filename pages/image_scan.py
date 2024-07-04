import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import io, os
import requests
from PIL import Image

load_dotenv()

#Read image from the url from user
st.title("SalesTrek - Image Scanner")
st.info("Please provide the link to the image you would like to scan.")

image_url = st.text_input("Image URL")

if st.button("Scan Image"):
    llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")
            # example
    message = HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": "What's in this image?",
                    },  # You can optionally provide text parts
                    {"type": "image_url", "image_url": image_url},
                ]
            )
    st.write(llm.invoke[message])
    