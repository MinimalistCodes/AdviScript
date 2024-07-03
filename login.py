import streamlit as st
from streamlit_supabase_auth import login_form, logout_button

# Load Supabase credentials from secrets
SUPABASE_URL = st.secrets["supabase_url"]
SUPABASE_KEY = st.secrets["supabase_api_key"]

# --- PAGE CONFIG ---
st.set_page_config(page_title="SalesTrek - Welcome, please login", page_icon="🔑")

# --- STYLING ---
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4; /* Light grey background */
            font-family: sans-serif;
        }
        .login-container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .login-container h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        .login-container input[type="text"],
        .login-container input[type="email"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .login-container button {
            background-color: #007bff; /* Primary color */
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- MAIN CONTENT ---
with st.container():  # Center the content
    st.image("your_logo.png")  # Replace with your actual logo path
    with st.form("login_form"):
        st.markdown("<div class='login-container'>", unsafe_allow_html=True)
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.form_submit_button("Login"):
            session = login_form(url=SUPABASE_URL, api_key=SUPABASE_KEY, providers=["apple", "facebook", "github", "google"])
            if session:
                st.success(f"Logged in as {session['user']['email']}")
                # Redirect to your main app page (replace 'main_app.py' with the actual filename)
                st.experimental_rerun()  # Refresh to trigger redirection
            else:
                st.error("Incorrect username or password")
        st.markdown("</div>", unsafe_allow_html=True)  # Close the login container
