import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'] # Default selected values
)

st.write('You selected: ', options)
