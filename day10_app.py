import streamlit as st

st.header('st.seletbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green')
)

st.write('Your favorite color is ', option)
