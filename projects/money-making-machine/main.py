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


def fetch_side_hutles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code ==200:
            hustles = response.json()
            return hustles
        else:
            return st.w
    except:
        return st.write("Something went wrong")

