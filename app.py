import streamlit as st

st.set_page_config(
    page_title="Customer Churn",
    page_icon=":hand",
    layout="wide",
    initial_sidebar_state="expanded"
)
#Main Content
st.title("Customer Churn App")
st.markdown("""
            This app uses machine learning models to generate customer churn data
            """)

# Key Features
st.subheader("Key Features")
st.markdown("""
            -Predicts customer churn based on various feature selections.
            -Provides a user friendly interface for easy navigation.
            -The app provides a detailed report on the performance of models used.
            """)

# App usage
st.subheader("Navigation")
st.markdown("""
            -Click on the tabs at the side to navigate through different pages.
            -Upload your csv file containing customer data.
            """)
