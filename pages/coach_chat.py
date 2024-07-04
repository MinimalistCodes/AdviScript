import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize OpenAI model with session state for persistence
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = OpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize conversation chain with session state for persistence
if "chain" not in st.session_state:
    st.session_state.chain = ConversationChain(llm=st.session_state["openai_model"])

# App UI
st.title("SalesTrek - Your AI Sales Coach 💬")

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What is your sales query?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Generate response from the conversation chain
    response = st.session_state.chain.run(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Store the conversation history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})

# Initialize session state for messages if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []
