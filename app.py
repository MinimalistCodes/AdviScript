import streamlit as st
import genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-pro")

# Function to generate the cold call script
def cold_script(industry):
    return f"""
Please generate a cold call script tailored for a sales representative calling potential customers in the {industry} industry. Include a structured call-flow, handle objections, and provide rebuttals both implied and explicitly handled within the script. The script should aim to engage prospects effectively, highlight key benefits of our product/service, and encourage further conversation or action.
"""

# Function for AI chatbot interaction (modified)
def ai_chatbot(message, history=None):
    if history is None:
        history = []
    history.append({"role": "user", "content": message})
    prompt = cold_script(message)  # Assuming 'message' is the industry here
    response = model.generate_text(prompt=prompt, max_length=1000, temperature=0.5)
    history.append({"role": "assistant", "content": response})
    return history, response

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI and Chat Logic
st.title("AdviScript: AI-Powered Sales Script Generator")
st.write("Select industry and start chatting to generate a cold call script.")

with st.form("input_form"):
    industry = st.selectbox(
        "Select Industry:",
        ["Technology", "Finance", "Healthcare", "Education", "Other"]
    )
    submitted = st.form_submit_button("Generate Script")

if submitted:
    st.session_state.messages, response = ai_chatbot(industry, st.session_state.messages)  

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
