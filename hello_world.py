"""
This is a simple hello world program using streamlit
"""
import time
import streamlit as st
import pandas as pd
import numpy as np

st.title("Test Simple Text Writing")
st.write("Hello world")
st.write("Test Changes")


st.title("Static Table with st.write")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

st.title("Static Table")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=(f'col {i}' for i in range(20))) # 10 rows, 20 columns

# Highlight max value in each column, For Row Change Axis to 1
st.dataframe(dataframe.style.highlight_max(axis=0))

st.title("Line Graph")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.title("Map")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.title("Slider")

x = st.slider('x', key='x')  # 👈 this is a widget
st.slider('y', key='y')
st.write(x, 'squared is', x * x)
st.write(st.session_state.y , 'squared is', st.session_state.y  * st.session_state.y )

st.title("Text Box")

st.text_input("Your name", key="name")
if st.session_state.name:
    st.write("Hello", st.session_state.name)

st.title("Setting Session State")

def form_callback():
    """Proving how Form Upload Callback Works"""
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    st.write(st.session_state.my_slider)
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    st.write(st.session_state.my_checkbox)
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

st.title("Select Box")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

st.write('You selected: ', option)

st.title("Expander")

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")


st.title("Progress")

# Add a placeholder
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.1)

st.title("Checkbox")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    st.write(chart_data)