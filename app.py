import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
#save to pdf
#save to docx


from dotenv import load_dotenv
import os, sys

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def ai_sales_coach(user_input):
    prompt = f"""
    You are an expert sales coach. You can help with various aspects of sales, including:

    *   Generating cold call scripts
    *   Crafting effective email templates
    *   Providing advice on handling objections
    *   Offering tips for closing deals
    *   Suggesting strategies for prospecting and lead generation
    *   Guiding sales presentations and demos
    *   Sharing best practices for building customer relationships
    *   Explaining sales methodologies and frameworks

    Please provide a comprehensive response to the following request:

    {user_input}
    """
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    return llm.invoke(prompt)


# UI and Chat Logic
st.title('Advi Script - Your AI Sales Coach')
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")

# Custom CSS for ChatGPT-like styling
st.markdown("""
<style>
.sidebar .sidebar-content {
    background-color: #F8F9FA; /* Light background */
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    overflow-y: auto;
    max-height: 500px; 
}
.chat-container {
    background-color: #FFFFFF; /* White background for main chat area */
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    overflow-y: auto; /* Enable scrolling */
    max-height: 500px;  /* Set maximum height */
}
.user-message, .bot-message {
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
}
.user-message {
    background-color: #E2F0FF; /* Light blue */
    text-align: right;
}
.bot-message {
    background-color: #F0F0F0; /* Light gray */
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# Chat History in Sidebar
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar.container(): 
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Main Chat Area
with st.container():  # Use container for styling
    if prompt := st.chat_input("Your message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = ai_sales_coach(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
                        
