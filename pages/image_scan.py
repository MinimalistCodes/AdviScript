import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import requests
from IPython.display import Image
import io
from PIL import Image


def image_scanner():
    st.title("Image Scanner")

    # Check if user is authorized (has paid)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(bytes_data))
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        if prompt := st.text_input("Ask the AI about the image:"):
                # image_url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
            message = HumanMessage(
                content=[prompt],
                role="user",
                source="streamlit",
                timestamp=None,
            )
            llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")
            response = llm.chat(message)
            st.write(response.content)
        else:
            st.write("Please provide a question about the image.")
    else:
        st.write("Please upload an image to scan.")
        

# Run the image scanner
image_scanner()
