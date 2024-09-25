// Streamlit application code 
import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is a basic Streamlit application.')

number = st.number_input('Pick a number', 0, 100)
st.write('You selected:', number)
