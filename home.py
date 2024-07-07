import streamlit as st
from utils import ai_sales_coach, script_gen, email_gen

# Load CSS file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main app function
def app():
    st.sidebar.title("SalesTrek AI Coach")
    st.title("Welcome to SalesTrek AI Coach")
    
    # Initialize session state for storing chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Display chat history
    for message in st.session_state.history:
        st.markdown(f"<div class='chat-message user-message'>{message['user']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-message bot-message'>{message['bot']}</div>", unsafe_allow_html=True)

    # Input box for user commands
    user_input = st.text_input("You:", key="user_input")

    if user_input:
        # Determine which function to call based on user input
        if "/script" in user_input:
            response = script_gen(user_input.replace("/script", "").strip())
        elif "/email" in user_input:
            response = email_gen(user_input.replace("/email", "").strip())
        else:
            response = ai_sales_coach(user_input)

        # Store the user input and bot response in session state
        st.session_state.history.append({"user": user_input, "bot": response})

        # Clear the input box
        st.session_state.user_input = ""

        # Refresh the page to display the new messages
        st.experimental_rerun()

# Run the app
if __name__ == "__main__":
    app()
