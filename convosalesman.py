from langchain_google_genai import GoogleGenerativeAI
import streamlit as st

st.title("ChatGPT-like clone")

# Initialize the GoogleGenerativeAI client with the API key
client = GoogleGenerativeAI(api_key=st.secrets["GOOGLE_API_KEY"])

# Set the default model if not already set in the session state
if "google_model" not in st.session_state:
    st.session_state["google_model"] = "gpt-3.5-turbo"

# Initialize an empty list for messages if not already set in the session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input for new messages
if prompt := st.chat_input("What is up?"):
    # Append the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response using GoogleGenerativeAI
    with st.chat_message("assistant"):
        response = client.generate(
            model=st.session_state["google_model"],
            prompt=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stop_sequences=["\n"],
            temperature=0.9,
            max_tokens=150,
        )
        # Display the generated response
        st.markdown(response)
        # Append the assistant's response to the session state
        st.session_state.messages.append({"role": "assistant", "content": response})