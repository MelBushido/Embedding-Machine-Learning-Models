import streamlit as st
import pandas as pd
import plotly.express as px

# -- Set up page configuration
st.set_page_config(page_title="EDA & Analytics Dashboard", page_icon=":bar_chart:", layout="wide")

# -- Simple authentication
def authenticate(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False

# -- Main function for the app
def main():
    st.title("EDA & Analytics Dashboard")
    st.write("Welcome to the comprehensive dashboard for Exploratory Data Analysis and Analytics!")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Select Dashboard", ("EDA Dashboard", "Analytics Dashboard"))

    # Load dataset
    df = load_data()

    if option == "EDA Dashboard":
        eda_dashboard(df)
    elif option == "Analytics Dashboard":
        analytics_dashboard(df)

# -- Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\user\Documents\New folder\LP.2\LP.2\Notebooks\churn_analysis.csv")
    return df

# -- EDA Dashboard
def eda_dashboard(df):
    st.header("Exploratory Data Analysis")

    # Show dataset
    st.subheader("Dataset")
    st.write(df.head())

    # Distribution of a selected column
    st.subheader("Column Distribution")
    column = st.selectbox("Select a column for distribution", df.columns)
    fig = px.histogram(df, x=column, title=f'Distribution of {column}')
    st.plotly_chart(fig)

    # Scatter plot between two selected columns
    st.subheader("Scatter Plot")
    x_column = st.selectbox("Select X-axis column", df.columns)
    y_column = st.selectbox("Select Y-axis column", df.columns, index=1)
    fig = px.scatter(df, x=x_column, y=y_column, title=f'Scatter Plot between {x_column} and {y_column}')
    st.plotly_chart(fig)

    # Box plot for a selected column
    st.subheader("Box Plot")
    box_column = st.selectbox("Select a column for box plot", df.columns)
    fig = px.box(df, y=box_column, title=f'Box Plot of {box_column}')
    st.plotly_chart(fig)

# -- Analytics Dashboard
def analytics_dashboard(df):
    st.header("Analytics Dashboard")

    # Display KPIs
    st.subheader("Key Performance Indicators")
    
    total_rows = df.shape[0]
    total_columns = df.shape[1]
    churn_rate = df['Churn'].value_counts(normalize=True).get('Yes', 0) * 100
    avg_monthly_charges = df['MonthlyCharges'].mean()

    st.metric(label="Total Customers", value=total_rows)
    st.metric(label="Total Features", value=total_columns)
    st.metric(label="Churn Rate (%)", value=f"{churn_rate:.2f}")
    st.metric(label="Average Monthly Charges", value=f"${avg_monthly_charges:.2f}")

    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    corr = df.corr(numeric_only=True)
    fig = px.imshow(corr, text_auto=True, aspect="auto", title="Correlation Heatmap")
    st.plotly_chart(fig)

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

# -- Authentication check
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.sidebar.success("Login successful!")
        else:
            st.sidebar.error("Invalid username or password")
else:
    main()