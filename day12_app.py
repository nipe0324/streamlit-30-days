import streamlit as st

st.header('st.checkbox')

st.write('What would you like to order?')

icecream = st.checkbox('Ice creame')
coffee = st.checkbox('Cofeee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
