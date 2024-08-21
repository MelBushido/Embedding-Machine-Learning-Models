import streamlit as st

# Page configuration
st.set_page_config(page_title="Customer Churn Prediction", page_icon="📈", layout="centered")

# CSS styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .login-box {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 400px;
        margin: auto;
    }
    .btn-login {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
    }
    .btn-login:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main title
st.title("Customer Churn Prediction App")

# Login section
with st.form(key='login_form'):
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.form_submit_button("Login")

    if login_button:
        if username == "admin" and password == "password":  
            st.success("Welcome, Admin!")
        else:
            st.error("Invalid credentials. Please try again.")

# Contact Us section
st.subheader("Contact Us")
with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_contact = st.form_submit_button("Submit")

    if submit_contact:
        st.success("Thank you for reaching out! We'll get back to you soon.")

# About Team section
st.subheader("About the Team")
st.markdown(
    """
    We are a team of data scientists dedicated to helping promote business growth. Our mission is to provide insights that help 
    companies grow using tools for analysis.
    """
)

# Display email for further inquiries
st.subheader("For further inquiries, contact us at:")
st.markdown("📧 Email: support@teamluxembourg.com")

# Footer
st.markdown("---")
st.markdown("© Team Luxembourg. All rights reserved.")

