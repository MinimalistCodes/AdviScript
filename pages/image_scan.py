import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import io, os
import requests
from PIL import Image

load_dotenv()

#Read uploaded image or url from user
st.title("SalesTrek - Image Scanner")
st.info("Upload an image and AI will tell you what it sees in the image.")
image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if image:
    image = Image.open(image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    image = image.convert("RGB")
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="JPEG")
    image_bytes = image_bytes.getvalue()
    api_key = os.getenv("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")
    message = HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": "What's the text in this image?",
                        "text": "What's in this image?",
                        "text": "Describe this image.",
                    },  # You can optionally provide text parts
                    {"type": "image_url", "url": image_bytes},
                ]
            )
    llm.invoke([message])
                


    
