from langchain import PromptTemplate
from langchain.document_loaders import WebBaseLoader
from langchain.schema import StrOutputParser
from langchain.schema.prompt_template import format_document
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI

import streamlit as st
import os
    
# Load environment variables

api_key = os.getenv("GOOGLE_API_KEY")

def summarize_text_or_url(input_value):
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    if input_value.startswith("http"):
        document = WebBaseLoader().load(input_value)
    else:
        document = input_value
    prompt = PromptTemplate("summarize", document=document)
    response = llm(prompt)
    summary = StrOutputParser().parse(response)
    return summary


# UI Layout
def app():
    st.title("Summarizer")
    st.write("Paste the text you want to summarize or enter a URL below:")

    # Input Text Area (allow multiple lines for URLs)
    input_value = st.text_area("Enter text or URL here", height=100)

    # Summarize Button
    if st.button("Summarize"):
        if input_value:
            with st.spinner("Summarizing..."):
                summary = summarize_text_or_url(input_value)
                st.subheader("Summary")
                st.write(summary)
        else:
            st.warning("Please enter text or a URL to summarize.")
app()

