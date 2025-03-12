import streamlit as st
import random
import requests
import time
st.title("Money Making Machine")

def generate_money ():
    return random.randint(1,10000)
st.subheader("Instant Money Generating Machine")
if st.button("Generate Money"):
    st.write("Counting Money...")
    time.sleep(5)
    amount = generate_money()
    st.success(f"You made ${amount} today!😍")

