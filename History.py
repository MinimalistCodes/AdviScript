import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


#All chat history 
st.session_state.stored_messages = json.dumps(st.session_state.messages)

