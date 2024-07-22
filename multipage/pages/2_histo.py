"""
Showing Histogram Data
"""
import streamlit as st
import numpy as np

if 'data' in st.session_state and not st.session_state.data.empty:
    data = st.session_state.data
    hist_values = np.histogram(data["date/time"].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)
