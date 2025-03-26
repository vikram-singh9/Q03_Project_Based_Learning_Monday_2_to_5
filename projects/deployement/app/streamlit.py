import streamlit as st

user  = st.text_input("Enter text: ")

if st.button("Submit"):
    st.write("You entered: ", user)