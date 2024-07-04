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
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    return llm.invoke(prompt)


# UI Layout
st.title("SalesTrek - Script Generator")
st.markdown("Ask any sales-related questions or request assistance with specific tasks.")
st.markdown("<small>Chat history is saved in your browser's local storage.</small>", unsafe_allow_html=True)

# UI Layout
st.markdown(
    """
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons" />
    """,
    unsafe_allow_html=True,
)

# MUI CSS (add this to your existing <style> section)
st.markdown(
    """
    <style>
    .MuiTextField-root {
        width: calc(100% - 30px); 
        resize: vertical;
        min-height: 40px;
        max-height: 200px; 
    }
    #chat-area {  
        flex-grow: 1; 
        overflow-y: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display 

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Load chat history from local storage
    try:
        stored_messages = st.session_state.get("stored_messages", None)
        if stored_messages:
            st.session_state.messages = json.loads(stored_messages)
    except json.JSONDecodeError:
        st.error("Error loading chat history from local storage.")


# Main Chat Area
with st.container():
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # MUI Input Field 
    st.markdown(
        """
        <div id="chat-input-container">
            <div id="chat-input"></div> 
        </div>
        <script>
        const chatInput = document.getElementById('chat-input');

        // Create and configure the MUI TextField
        const textField = new window['MaterialUI'].TextField({
            label: 'Your message',
            variant: 'outlined',
            fullWidth: true,
            multiline: true,
            rows: 2,
            InputProps: {
                style: { fontSize: '16px', padding: '10px' },  // Customize font size and padding
            },
            onChange: (event) => {
                window.Streamlit.setComponentValue("chat_input", event.target.value);
            }
        });

        // Render the TextField to the chatInput div
        window['ReactDOM'].render(textField, chatInput);
        </script>
        """,
        unsafe_allow_html=True,
    )

    # Input Handling (modified)
    if st.session_state.get("chat_input"):
        user_input = st.session_state["chat_input"]
        del st.session_state["chat_input"]  # Clear the input

        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
    # Display "Sales Coach is typing..."
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

    # Get and append AI response (with a delay to simulate typing)


st.session_state.stored_messages = json.dumps(st.session_state.messages)