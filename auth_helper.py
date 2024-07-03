# auth_utils.py
import streamlit as st
import auth

def check_and_display_auth():
    """Checks authentication and displays login/logout UI."""
    if not auth.is_logged_in():
        st.title("Please Login")  
        auth.login()
        st.stop()  # Stop execution until login is successful
    else:
        # User is logged in
        user = auth.get_current_user()
        with st.sidebar:
            st.write(f"Welcome, {user['email']}!")
            if st.button("Logout"):
                auth.logout()
                st.experimental_rerun()  # Refresh the page after logout

def requires_auth(func):
    """Decorator to require authentication for a Streamlit page."""
    def wrapper(*args, **kwargs):
        check_and_display_auth()
        return func(*args, **kwargs)  # Call the decorated function after auth check
    return wrapper
