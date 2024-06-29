import streamlit as st
from google.generativeai import GenerativeModel
from google.api_core import retry

# Authenticate with your Gemini Pro API key
GEMINI_MODEL = "models/gemini-pro" 
client = GenerativeModel.from_pretrained(GEMINI_MODEL, api_key='YOUR_API_KEY')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []# Styling the chat window
st.markdown("""
<style>
.chat-message {
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 5px;
}
.user-message {
    background-color: #2e8b57; /* Green for user */
    color: white;
    text-align: right; /* Align user messages to the right */
}
.bot-message {
    background-color: #34495e; /* Blue for bot */
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Display chat messages from history on initial load
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Input prompt
if prompt := st.chat_input("Your message"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate bot's response
    @retry.Retry()
    def generate_response():
        response = client.generate_text(
            prompt=f"Human: {prompt}\nAssistant:",
            temperature=0.7,
            max_output_tokens=1024
        )
        return response.result

    bot_response = generate_response()

    # Add bot message to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    # Display bot message in chat
    with st.chat_message("assistant"):
        st.markdown(bot_response)
