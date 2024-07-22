"""
Test the cache functionality
"""
import streamlit as st
import pandas as pd

def load_data(url):
    """
    Loading Data From URL
    """
    df = pd.read_csv(url)  # 👈 Download the data
    return df

data = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(data)

st.button("Rerun")
