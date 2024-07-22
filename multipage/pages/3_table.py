"""
Streamlit Table
"""
import streamlit as st

if st.session_state.number:
    st.write(f"Number: {st.session_state.number}")
if 'data' in st.session_state and not st.session_state.data.empty:
    st.table(st.session_state.data)
else:
    st.write("No data to display. Please run the homepage script.")
