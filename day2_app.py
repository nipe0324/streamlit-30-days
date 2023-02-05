import streamlit as st

st.header('st.buttton')

if st.button('Say hello'):
    st.write('Why hello ther')
else:
    st.write('Goodbye')
