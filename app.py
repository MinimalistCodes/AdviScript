import streamlit as st
from google.generativeai import GenerativeModel
from google.api_core import retry

# 1. Load API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# 2. Authenticate with Gemini Pro
GEMINI_MODEL = "models/gemini-pro"
client = GenerativeModel.from_pretrained(GEMINI_MODEL, api_key=api_key)


# Initialize chat history and industry variable
if "messages" not in st.session_state:
    st.session_state.messages = []
if "industry" not in st.session_state:
    st.session_state.industry = ""

# Styling the chat window (same as before)
...

# --- Display chat messages from history on initial load ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Input prompt & industry selection ---
col1, col2 = st.columns(2)
with col1:
    if prompt := st.chat_input("Your message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

with col2:
    industry = st.selectbox(
        "Select Industry:",
        ["Technology", "Finance", "Healthcare", "Education", "Other"]
    )
    if st.session_state.industry != industry:
        st.session_state.industry = industry

# --- Generate bot's response ---
@retry.Retry()
def generate_response():
    prompt = f"""Please generate a cold call script tailored for a sales representative 
                 calling potential customers in the {st.session_state.industry} industry. 
                 Include a structured call-flow, handle objections, and provide rebuttals 
                 both implied and explicitly handled within the script. The script should aim to 
                 engage prospects effectively, highlight key benefits of our product/service, 
                 and encourage further conversation or action. """
    response = client.generate_text(
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=1024
    )
    return response.result

if prompt:
    bot_response = generate_response()

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# --- Instructions or tips for using the chatbot ---
with st.expander("Tips"):
    st.write("Select the industry you're targeting before asking for a script.")
    st.write("Be as descriptive as possible to get the best results.")
