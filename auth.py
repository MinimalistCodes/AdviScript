import streamlit as st
from streamlit_supabase_auth import login_form, logout_button


def main():
     # Your app's main content here

    st.markdown(
        """
        <style>
            /* Overall Login Page Styling */
            body {
                background-color: #f5f5f5; /* Light gray background */
                font-family: "Helvetica Neue", Arial, sans-serif;
            }

            /* Centered Form Container */
            .login-container {
                max-width: 400px;
                margin: 100px auto; /* Center horizontally and add top margin */
                padding: 30px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
            }

            /* Form Title */
            .login-container h2 {
                text-align: center;
                margin-bottom: 20px;
                color: #333;
            }

            /* Input Fields */
            .login-container input[type="email"],
            .login-container input[type="password"] {
                width: calc(100% - 22px);
                padding: 15px;
                margin-bottom: 20px;
                border: 1px solid #ddd;
                border-radius: 5px;
                box-sizing: border-box;
            }

            /* Login Button */
            .login-container button[type="submit"] {
                background-color: #007bff; /* Blue */
                color: white;
                padding: 15px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
                font-size: 16px;
            }

            /* Hover effect for the button */
            .login-container button[type="submit"]:hover {
                background-color: #0056b3; /* Darker blue on hover */
            }

            /* Error Message Styling */
            .st-supabase-auth .error {
                color: red;
                margin-top: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
        st.title("Welcome to SalesTrek!")
    st.header("Login with Supabase Auth")
    session = login_form(providers=["apple", "facebook", "github", "google"])
    st.write(session)
    if not session:
        return
    st.experimental_set_query_params(page=["success"])
    with st.sidebar:
        st.write(f"Welcome {session['user']['email']}")
        logout_button()


if __name__ == "__main__":
    main()