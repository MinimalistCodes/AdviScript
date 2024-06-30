import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os, sys


# Load environment variables
load_dotenv()

# Configure Google Gemini API - Remove this section as we will use langchain
# google_genai = GoogleGenAI(api_key=os.getenv("GOOGLE_API_KEY"))
api_key = os.getenv("GOOGLE_API_KEY")

# Function to generate the cold call script
def cold_script(industry):
    return f"""
Please generate a cold call script tailored for a sales representative calling potential customers in the {industry} industry. Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""

# Function for AI chatbot interaction using langchain
def ai_chatbot(industry):
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)
    prompt = cold_script(industry)
    template = PromptTemplate(prompt)
    response = llm.invoke(template)
    st.session_state.messages.append({"role": "assistant", "content": response})
    return response

    
    


# Main function
def main():
    st.title("Cold Call Script Generator")
    st.write("Welcome to the Cold Call Script Generator! Please enter the industry you are targeting and let the AI generate a cold call script for you.")

    industry = st.text_input("Enter the industry you are targeting:")
    if st.button("Generate Cold Call Script"):
        st.session_state.messages = []
        st.session_state.messages.append({"role": "user", "content": industry})
        ai_chatbot(industry)
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.write(f"User: {message['content']}")
            else:
                st.write(f"Assistant: {message['content']}")
                
if __name__ == "__main__":
    main()



