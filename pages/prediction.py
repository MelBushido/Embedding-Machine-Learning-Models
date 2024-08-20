import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
import requests
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
import joblib
import imblearn
import os

# Configure the page
st.set_page_config(
    page_title='Predictions',
    page_icon='🔮',
    layout='wide'
)

st.title("Predict Customer Churn!")

# URLs for loading models and encoder from GitHub (Ensure these are direct links to the raw files)
github_model1_url = 'https://github.com/MelBushido/LP.2/raw/main/model/GradientBoosting.joblib'
github_model2_url = 'https://github.com/MelBushido/LP.2/raw/main/model/SupportVector.joblib'
encoder_url = 'https://github.com/MelBushido/LP.2/raw/main/model/label_encoder.joblib'

# Function to load the model from GitHub
@st.cache_resource(show_spinner="Loading model")
def load_model(url):
    response = requests.get(url)
    model_bytes = BytesIO(response.content)
    model = joblib.load(model_bytes)
    return model

# Function to load encoder from GitHub
@st.cache_resource(show_spinner="Loading encoder")
def load_encoder():
    response = requests.get(encoder_url)
    encoder_bytes = BytesIO(response.content)
    encoder = joblib.load(encoder_bytes)
    return encoder

# Function for model selection
def select_model(model_option):
    if model_option == 'Gradient Boosting':
        model = load_model(github_model1_url)
    elif model_option == 'Support Vector':
        model = load_model(github_model2_url)
    encoder = load_encoder()
    return model, encoder

# Custom transformer classes
class TotalCharges_cleaner(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['TotalCharges'].replace(' ', np.nan, inplace=True)
        X['TotalCharges'] = X['TotalCharges'].astype(float)
        return X

class columnDropper(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop('customerID', axis=1)

# Initialize prediction in session state
if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
if 'prediction_proba' not in st.session_state:
    st.session_state['prediction_proba'] = None

# Function to make predictions
def make_prediction(model, encoder):
    data = pd.DataFrame([[
        st.session_state['customer_id'], st.session_state['gender'], st.session_state['senior_citizen'], 
        st.session_state['partners'], st.session_state['dependents'], st.session_state['tenure'],
        st.session_state['phone_service'], st.session_state['multiple_lines'], st.session_state['internet_service'],
        st.session_state['online_security'], st.session_state['online_backup'], st.session_state['device_protection'],
        st.session_state['tech_support'], st.session_state['streaming_tv'], st.session_state['streaming_movies'],
        st.session_state['contract'], st.session_state['paperless_billing'], st.session_state['payment_method'],
        st.session_state['monthly_charges'], st.session_state['total_charges']
    ]], columns=[
        'customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 
        'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 
        'PaymentMethod', 'MonthlyCharges', 'TotalCharges'
    ])

    prediction = model.predict(data)
    prediction = encoder.inverse_transform(prediction)
    st.session_state['prediction'] = prediction

    prediction_proba = model.predict_proba(data)
    st.session_state['prediction_proba'] = prediction_proba

    data['Churn'] = prediction
    data['Model'] = st.session_state['model_option']

    return prediction, prediction_proba

# Input features form
def input_features():
    with st.form('features'):
        model_pipeline, encoder = select_model(st.session_state['model_option'])
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Demographics')
            st.text_input('Customer ID', value="", placeholder='e.g., 1234-ABCDE', key='customer_id')
            st.radio('Gender', options=['Male', 'Female'], horizontal=True, key='gender')
            st.radio('Partner', options=['Yes', 'No'], horizontal=True, key='partners')
            st.radio('Dependents', options=['Yes', 'No'], horizontal=True, key='dependents')
            st.radio("Senior Citizen (Yes-1, No-0)", options=[1, 0], horizontal=True, key='senior_citizen')

        with col1:
            st.subheader('Customer Account Info.')
            st.number_input('Tenure', min_value=0, max_value=70, key='tenure')
            st.selectbox('Contract', options=['Month-to-month', 'One year', 'Two year'], key='contract')
            st.selectbox('Payment Method',
                         options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'],
                         key='payment_method')
            st.radio('Paperless Billing', ['Yes', 'No'], horizontal=True, key='paperless_billing')
            st.number_input('Monthly Charges', placeholder='Enter amount...', key='monthly_charges')
            st.number_input('Total Charges', placeholder='Enter amount...', key='total_charges')

        with col2:
            st.subheader('Subscriptions')
            st.radio('Phone Service', ['Yes', 'No'], horizontal=True, key='phone_service')
            st.selectbox('Multiple Lines', ['Yes', 'No', 'No internet service'], key='multiple_lines')
            st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'], key='internet_service')
            st.selectbox('Online Security', ['Yes', 'No', 'No internet service'], key='online_security')
            st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'], key='online_backup')
            st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'], key='device_protection')
            st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'], key='tech_support')
            st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'], key='streaming_tv')
            st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'], key='streaming_movies')

        submit_button = st.form_submit_button('Predict')
        if submit_button:
            make_prediction(model_pipeline, encoder)

if __name__ == '__main__':
    # Model selection form
    with st.form(key='model_selection_form'):
        st.selectbox(
            label='Choose which model to use for prediction',
            options=['Gradient Boosting', 'Support Vector'],
            key='model_option'
        )
        st.form_submit_button(label='Submit')

    input_features()

    if st.session_state['prediction'] is not None:
        prediction = st.session_state['prediction']
        probability = st.session_state['prediction_proba']
        
        if prediction[0] == "Yes":
            st.markdown(f'### The customer will churn with a {round(probability[0][1], 2)} probability.')
        else:
            st.markdown(f'### The customer will not churn with a {round(probability[0][0], 2)} probability.')