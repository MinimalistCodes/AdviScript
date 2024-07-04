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
   
     
        
with st.container():
    if image_url := st.text_input("Image URL"):
        st.session_state.messages.append("role", "user", "content", image_url)
        
        with st.chat_message("user"):
            st.markdown(image_url)
            
        # Display image
        response = requests.get(image_url)
        image = Image.open(io.BytesIO(response.content))
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Scanning image...")
        
        # Scan image
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
        st.write(llm.invoke([message]))
        message_placeholder.markdown(response.content[0]["text"])
        
