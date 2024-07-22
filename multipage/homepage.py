"""
Streamlit Homepage
"""
import streamlit as st 
import pandas as pd
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    """
    Loading Data From URL
    """
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

st.title("Streamlit Homepage")

st.session_state.data = load_data(10000)
st.session_state.number = 15

if st.button("Next"):
    st.switch_page("pages/1_map.py")
