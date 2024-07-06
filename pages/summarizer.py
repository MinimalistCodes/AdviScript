import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Please set your GOOGLE_API_KEY in the .env file.")
    st.stop()

def summarize_url(url):
    try:
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
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading the URL: {e}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI
def app():
    st.title("URL Summarizer")
    st.write("Paste the URL of a web page to get a concise summary:")

    url = st.text_input("Enter URL")

    if st.button("Summarize"):
        if url:
            with st.spinner("Summarizing..."):
                summary = summarize_url(url)
                if summary:
                    st.subheader("Summary")
                    st.write(summary)
                else:
                    st.warning("Failed to summarize the URL. Please try again.")
        else:
            st.warning("Please enter a valid URL.")

# Run the app
if __name__ == "__main__":
    app()
