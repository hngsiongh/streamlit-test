"""
Create Test Uber App
"""
import streamlit as st
import pandas as pd
import numpy as np


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

st.title("Uber App")

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


st.sidebar.title('Sidebar')

st.sidebar.subheader('Filter Data By Hours')
hour = st.sidebar.slider('Hour', 0, 23)

data_loading_text = st.text("Preparing to Load Data")
data = load_data(10000)
data_loading_text.text("Data Loaded")

st.subheader('Raw data')
st.write(data)

st.subheader('Number of pickups by hour')

# Bins 24 Bins for 24 Hours, If I set bins to 12, I am just indicating each bin to have 2 hours of data.
# Range 0 to 24, indicating all hours from 0 to 24 to be included, If I change to range (12,24) it will only show from 12 to 24
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=12, range=(0,24))[0]
st.bar_chart(hist_values)

st.subheader('Map of all pickups')
# It detects the Lat Long and Just Prints it
st.map(data)

st.subheader("Busiest Hour Data")
HOUR = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == HOUR]
st.map(filtered_data)

st.subheader("SideBar Filtered Data")
slider_data = data[data[DATE_COLUMN].dt.hour == hour]
st.map(slider_data)
