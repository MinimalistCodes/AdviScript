import streamlit as st
from google.generativeai import TextService

# Load API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]
client = TextService(api_key=api_key)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Styling the chat window ---
# ... (same as before)

# --- Display chat messages from history on initial load ---
# ... (same as before)

# --- Input prompt & industry selection ---
# ... (same as before)

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
        model=GEMINI_MODEL,  # Replace with the actual model name if different
        prompt=prompt,
        temperature=0.7,
        max_output_tokens=1024
    )
    return response.text

if prompt:
    bot_response = generate_response()

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# --- Instructions or tips for using the chatbot ---
# ... (same as before)
