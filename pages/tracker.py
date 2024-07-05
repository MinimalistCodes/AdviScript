import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import pandas as pd 
import time
import json
import os
from fpdf import FPDF
import datetime

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# ... [other imports and functions remain the same]
# Initialize OpenAI model with session state for persistence
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = OpenAI(temperature=0.7, openai_api_key=api_key)

# Initialize conversation chain with session state for persistence
if "chain" not in st.session_state:
    st.session_state.chain = ConversationChain(llm=st.session_state["openai_model"])

# ... (Other parts of your code remain the same)


# UI Layout (same as before)

# Display time and date
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.markdown(f"**Chat History:** {formatted_time}")

# Chat History
if "activities" not in st.session_state:
    st.session_state.activities = []
    # Load activity history from local storage
    try:
        stored_activities = st.session_state.get("stored_activities", None)
        if stored_activities:
            st.session_state.activities = json.loads(stored_activities)
    except json.JSONDecodeError:
        st.error("Error loading activity history from local storage.")
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Load chat history from local storage
    try:
        stored_messages = st.session_state.get("stored_messages", None)
        if stored_messages:
            st.session_state.messages = json.loads(stored_messages)
    except json.JSONDecodeError:
        st.error("Error loading chat history from local storage.")


with st.container():  # Use container for styling
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input Box at the Bottom (Docked and Centered)
    with st.container():
        user_input = st.text_area("Your message", key="chat_input", height=40, on_change=None)
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            # Display "Sales Coach is thinking..." message
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                with st.status("Thinking...", expanded=True) as status:
                    st.write("Combing over resources...")
                    time.sleep(2)
                    st.write("Script finished")
                    time.sleep(1)
                    st.write("Sending script...")
                    time.sleep(1)  # Adjust the delay as needed
                    status.update(label="Crafting complete!", state="complete", expanded=False)
                    message_placeholder.markdown("Sales Coach is typing...")
                    response = ai_sales_coach(prompt)
                    message_placeholder.markdown(response)  # Update the placeholder
                    st.session_state.messages.append({"role": "assistant", "content": response})

            # Clear the input box after sending the message
            st.session_state.chat_input = ""

            # Save chat history to local storage
            st.session_state.stored_messages = json.dumps(st.session_state.messages)


# Buttons in a Row (under the input box)
with st.container():
    st.markdown("<div id='button-container'>", unsafe_allow_html=True)  # Button container
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear History"):
            # Clear chat history (same as before)
            st.session_state.messages = []
            st.session_state.pop("stored_messages", None)
            st.experimental_rerun()

    with col2:
        if st.button("Export Chat to PDF"):
            # Export to PDF (same as before)
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for message in st.session_state.messages:
                role = message["role"].capitalize()
                content = message["content"]
                pdf.cell(200, 10, txt=f"{role}: {content}", ln=True, align="L")

            pdf_output = pdf.output(dest="S").encode("latin-1")
            st.download_button(
                label="Download PDF",
                data=pdf_output,
                file_name="chat_history.pdf",
                mime="application/pdf",
            )
    st.markdown("</div>", unsafe_allow_html=True)  # Close button container
with st.expander("See Activity Log"):
    # Display Logged Activities
    st.subheader("Logged Activities")
    if st.session_state.activities:
        df = pd.DataFrame(st.session_state.activities)
        st.dataframe(df, use_container_width=True)  # Display as a table
    else:
        st.write("No activities logged yet.")
