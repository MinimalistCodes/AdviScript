import streamlit as st
from google.cloud import aiplatform
from dotenv import load_dotenv
import io
from PIL import Image
import os

load_dotenv()

# Project Configuration (Load from environment variables)
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
api_key = os.getenv("GOOGLE_API_KEY")

# Function to analyze the image
def analyze_image(image_data, prompt):
    # Initialize the Vertex AI client
    aiplatform.init(project=PROJECT_ID, location=LOCATION)
    # Set API key for authentication
    genai.configure(api_key=api_key)

    with st.spinner("Analyzing Image..."):
        image = aiplatform.Image(bytes=image_data)
        response = llm.generate_content(
            [
                aiplatform.types.content.TextGenerationContent(text=prompt),
                aiplatform.types.content.ImageGenerationContent(image=image),
            ]
        )

        # Handle the response
        try:
            return response.predictions[0].content
        except Exception as e:
            st.error(f"Error analyzing image: {e}")
            return "Sorry, I couldn't analyze the image at this time. Please try again later."

# UI Layout
def app():
    st.title("SalesTrek - Image Scanner")
    st.info("Please upload the image you would like to scan.")

    # File Uploader
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(bytes_data))
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        # Question Input
        prompt = st.text_area("Enter your question about the image:")
        
        # Analyze Button
        if st.button("Analyze"):
            if prompt:
                with st.spinner("Analyzing..."):
                    response = analyze_image(bytes_data, prompt)
                    st.write(response)
            else:
                st.warning("Please enter a question.")

# Model Initialization
llm = aiplatform.gapic.PredictionServiceClient().generate_content


if __name__ == "__main__":
    app()
