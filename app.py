import time
import streamlit as st
from dotenv import load_dotenv
import os, sys, json

from transformers import AutoTokenizer, AutoModelForCausalLM

# Choose a suitable model name (e.g., "EleutherAI/gpt-neo-125M")
model_name = "EleutherAI/gpt-neo-125M" 

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

LLM_MODELS = {
    "GPT-Neo 125M": "EleutherAI/gpt-neo-125M",
    "DialoGPT-medium": "microsoft/DialoGPT-medium",
    "Flan-T5-base": "google/flan-t5-base",
    # Add more models as needed
}

def load_model_and_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

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
    *   Assisting with sales training and coaching
    *   Team building and motivation
    *   Sales management and leadership
    *   Tracking and analyzing sales performance
    *   Sales exercises and role-playing scenarios
    *   Sales forecasting and pipeline management
    *   Sales negotiation tactics and strategies
    *   Recommendations for sales technology and tools
    *   Sales psychology, buyer behavior, and persuasion techniques
    *   Sales ethics and compliance
    *   Emotional intelligence in sales

    Please provide a comprehensive response to the following request:

    {user_input}
 """
    try:
            input_ids = tokenizer(prompt, return_tensors="pt").input_ids  # Tokenize the prompt
            output = model.generate(input_ids, max_length=1000)  # Generate the response
            return tokenizer.decode(output[0], skip_special_tokens=True)  # Decode the response
    except Exception as e:  
            st.error(f"An error occurred: {e}")  
            return "Sorry, I couldn't process your request at this time. Please try again later."


# UI Layout
st.title("Advi Script - Your AI Sales Coach")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")

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
#chat-area {  /* Container for chat messages */
    flex-grow: 1; /* Allow chat area to expand to fill available space */
    overflow-y: auto;  /* Enable scrolling in the chat area */
}
</style>
""", unsafe_allow_html=True)

# Chat History and Model Selection
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.model_name = "GPT-Neo 125M"  # Default model

    # Load chat history from local storage
    try:
        stored_messages = st.session_state.get("stored_messages", None)
        if stored_messages:
            st.session_state.messages = json.loads(stored_messages)
    except json.JSONDecodeError:
        st.error("Error loading chat history from local storage.")


with st.sidebar:
    st.markdown("**Model Selection**")
    selected_model = st.selectbox("Choose a model:", list(LLM_MODELS.keys()), key="model_select")

    if selected_model != st.session_state.model_name:  # Model changed
        st.session_state.model_name = selected_model
        tokenizer, model = load_model_and_tokenizer(LLM_MODELS[selected_model]) 

with st.container():
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input Box at the Bottom (Docked and Centered)
    with st.container():  
        # Removed the button and form
        user_input = st.text_area("Your message", key="chat_input", height=40, on_change=None)
        if user_input:  # Check if Enter was pressed or text area changed significantly
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            # Display "Sales Coach is typing..." message
            with st.chat_message("assistant"):
                message_placeholder = st.empty() 
                message_placeholder.markdown("Sales Coach is typing...")

            # Get AI response with a slight delay to simulate typing
            time.sleep(1)  # Adjust delay as needed
            response = ai_sales_coach(user_input, model, tokenizer)
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Update the placeholder with the actual response
            message_placeholder.markdown(response) 

            # Clear the input box after sending the message
            st.session_state.chat_input = ""

            # Save chat history to local storage
            st.session_state.stored_messages = json.dumps(st.session_state.messages)