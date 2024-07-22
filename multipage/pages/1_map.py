"""
Showing Map Data
"""
import streamlit as st

if "data" in st.session_state and not st.session_state.data.empty:
    st.map(st.session_state.data)
