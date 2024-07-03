import time
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os, sys, json
from fpdf import FPDF
from streamlit_extras.switch_page_button import switch_page
from st_paywall import Paywall




# Load environment variables

api_key = os.getenv("GOOGLE_API_KEY")

def summarize_text_or_url(input_value):
    try:
        # Load the content
        if input_value.startswith("http"):  # It's a URL
            loader = WebBaseLoader(input_value)
            docs = loader.load()  # Load the web page content
        else:
            docs = [{"text": input_value}]  # Treat as plain text

        # Initialize LLM and summarization chain
        llm = GoogleGenerativeAI(temperature=0, google_api_key=api_key)
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""], chunk_size=1000, chunk_overlap=200
        )
        prompt = PromptTemplate(
            template="Write a concise summary of the following:\n{text}\nCONCISE SUMMARY:",
            input_variables=["text"]
        )
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

        # Invoke the summarization chain
        response = stuff_chain.run(docs)
        return response
    except Exception as e:
        st.error(f"Error: {e}")
        return "Sorry, I couldn't process the request. Please check the input or try again later."

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
