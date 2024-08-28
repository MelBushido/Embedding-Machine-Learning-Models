import streamlit as st
import pandas as pd

def history_page():
    # Title of the History Page
    st.title("History")

    # Load previous predictions from a CSV file
    csv_file_path = r"C:\Users\user\Documents\New folder\LP.4\Embedding-Machine-Learning-Models\data\history.csv"

    @st.cache_data
    def load_history():
        return pd.read_csv(csv_file_path)

    history_df = load_history()

    # Display the DataFrame
    st.subheader("Previous Predictions and Input Values")
    st.write(history_df)

    # Sorting Options
    if st.checkbox("Show Data Summary"):
        st.write(history_df.describe())

    if st.checkbox("Sort by Prediction"):
        sorted_df = history_df.sort_values(by="Prediction", ascending=False)
        st.write(sorted_df)

if __name__ == "__main__":
    history_page()
