import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def summarize_text_or_url(input_value, is_url=False):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    
    if is_url:
        loader = WebBaseLoader(url=input_value)
        docs = loader.load()
    else:
        docs = [input_value]
    
    template = """Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:"""

    prompt = PromptTemplate.from_template(template)

    llm_chain = LLMChain(llm=llm, prompt=prompt)
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

    response = stuff_chain.invoke(docs)
    return response["output_text"]
 
def app():
    st.title("Text/URL Summarizer")
    st.info("Either enter the text you want to summarize or paste in a url")
    # Input Type Selection
    input_type = st.radio("Choose input type:", ["Text", "URL"])

    if input_type == "Text":
        text_input = st.text_area("Enter text here", height=200)
        input_value = text_input
        is_url = False
    else:
        url_input = st.text_input("Enter URL:")
        input_value = url_input
        is_url = True

    # Summarize Button
    if st.button("Summarize"):
        if input_value:
            with st.spinner("Summarizing..."):
                summary = summarize_text_or_url(input_value, is_url)
                st.subheader("Summary")
                st.write(summary)
        else:
            st.warning("Please enter text or a URL to summarize.")

if __name__ == "__main__":
    app()