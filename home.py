import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Customer Churn App",
    page_icon=":hand:",  
    layout="wide",      
    initial_sidebar_state="expanded"  
)

# Main Content
st.title("Customer Churn Prediction App")
st.markdown("""
This application leverages advanced machine learning algorithms to predict customer churn, enabling businesses to identify at-risk customers and take proactive measures to retain them. The app is designed to be user-friendly, offering an intuitive interface that allows users to interact with the data and models seamlessly.
""")

# Key Features
st.subheader("Key Features")
st.markdown("""
- **Churn Prediction**: The core feature of this app is its ability to predict customer churn based on various input features like customer demographics, transaction history, and contract details.
- **Interactive Data Visualization**: Users can explore their data through interactive visualizations, including bar charts, pie charts, and correlation heatmaps.
- **Model Performance Evaluation**: The app provides detailed reports on the performance of different machine learning models, including accuracy, precision, recall, and F1-score, allowing users to compare and select the best model.
- **Customizable Input**: Users can upload their own datasets in CSV format and adjust the features used in the prediction models.
- **Real-time Predictions**: After uploading the data, users can generate predictions in real-time and download the results for further analysis.
""")

# How It Works
st.subheader("How It Works")
st.markdown("""
1. **Data Upload**: Start by uploading your CSV file containing customer data. Ensure that the data includes relevant columns such as customer demographics, subscription details, and transaction history.
2. **Data Exploration**: Use the interactive visualizations provided to explore the dataset. Identify patterns and correlations that might indicate customer churn.
3. **Model Selection**: Choose from a variety of pre-trained machine learning models. The app offers options like Logistic Regression, Decision Trees, Random Forest, and Gradient Boosting.
4. **Generate Predictions**: Run the selected model on your dataset to predict which customers are likely to churn. The app will output the predictions along with confidence scores.
5. **Review Results**: Examine the results and performance metrics. You can download the prediction results for further analysis or integration into other business tools.
""")

# App Usage
st.subheader("Navigation Guide")
st.markdown("""
- **Sidebar Navigation**: Use the sidebar to navigate through different sections of the app:
  - **Home**: Overview of the app and its features.
  - **Data Upload**: Upload your customer data in CSV format.
  - **Data Visualization**: Explore your data through interactive charts and graphs.
  - **Model Training**: Select pre trained machine learning models  on your dataset and evaluate their performance.
  - **Predictions**: Generate and review churn predictions.
  - **Download Results**: Export the prediction results and performance reports.
""")

# Contact Information
st.subheader("Contact & Support")
st.markdown("""
For assistance or to provide feedback, please reach out at:
- **Email**: daigurenfc@gmail.com
- **Github**: https://github.com/MelBushido/Embedding-Machine-Learning-Models
- **LinkedIn**: https://www.linkedin.com/in/melvin-suwiir-1318a4184/
""")