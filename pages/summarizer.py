import streamlit as st
from langchain.llms import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def summarize_url(url):
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

    loader = WebBaseLoader(url)
    docs = loader.load()

    template = """Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:"""

    prompt = PromptTemplate.from_template(template)

    llm_chain = LLMChain(llm=llm, prompt=prompt)
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

    response = stuff_chain.run(docs)
    return response["output_text"]
 
def app():
    st.title("URL Summarizer")
    st.info("Paste the URL of the web page you want to summarize:")

    # URL Input
    url_input = st.text_input("Enter URL:")

    # Summarize Button
    if st.button("Summarize"):
        if url_input:
            with st.spinner("Summarizing..."):
                summary = summarize_url(url_input)
                st.subheader("Summary")
                st.write(summary)
        else:
            st.warning("Please enter a URL to summarize.")
