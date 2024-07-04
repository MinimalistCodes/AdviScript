import time
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os, sys, json

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")


def ai_sales_coach(user_input):
  prompt = f"""
  You are an expert sales coach. And help sales representatives improve their skills, confidence, and goals to increase sales performance and build empowerment. 
  You'll work with individual companies to identify areas for improvement and develop plans to address them. 

  Please provide a comprehensive response to the following request:

  {user_input}
  """
  llm = GoogleGenerativeAI(model="gemini-pro", GOOGLE_API_KEY=api_key)
  return llm.invoke(prompt)


# UI Layout
st.title("SalesTrek - Script Generator")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
st.markdown("<small>Chat history is saved in your browser's local storage.</small>", unsafe_allow_html=True)

# Custom CSS for Gemini-like styling with full-screen chat and docked input
st.markdown("""
<style>
body {
  font-family: 'Arial', sans-serif; 
  display: flex; /* Use flexbox for layout */
  flex-direction: column; /* Arrange elements vertically */
  height: 100vh; /* Make the container take up full viewport height */
}
.chat-message {
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 10px;
  line-height: 1.5; 
}
.user-message {
  background-color: #F0F0F0; 
  text-align: right;
}
.bot-message {
  background-color: #FFFFFF;
  text-align: left;
}
#chat-input-container {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #FFFFFF;
  padding: 15px;
}
#chat-input { /* Style the textarea for input */
  width: calc(100% - 30px); /* Account for padding */
  resize: vertical; /* Allow vertical resizing */
  min-height: 40px; /* Minimum height */
  max-height: 200px; /* Maximum height */
}
#chat-area { /* Container for chat messages */
  flex-grow: 1; /* Allow chat area to expand to fill available space */
  overflow-y: auto; /* Enable scrolling in the chat area */
}
</style>
""", unsafe_allow_html=True)

# Chat History
if "messages" not in st.session_state:
  st.session_state.messages = []

  try:
    stored_messages = st.session_state.get("stored_messages", None)
    if stored_messages:
      st.session_state.messages = json.loads(stored_messages)
  except json.JSONDecodeError:
    st.error("Error loading chat history from local storage.")



with st.container(): # Use container for styling
  for message in st.session_state.messages:
      with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# User Input
if prompt := st.chat_input("Your message"):
  # Append user message to chat history
  st.session_state.messages.append({"role": "user", "content": prompt})
  
  # Display user message
  with st.chat_message("user"):
    st.markdown(prompt)

  # Display "Sales Coach is typing..."
  with st.chat_message("assistant"):
    message_placeholder = st.empty() 
    message_placeholder.markdown("Sales Coach is thinking...")
    response = ai_sales_coach(prompt)
    message_placeholder.markdown(response) # Update the placeholder
    st.session_state.messages.append({"role": "assistant", "content": response})

  # Get and append AI response (with a delay to simulate typing)


st.session_state.stored_messages = json.dumps(st.session_state.messages)
