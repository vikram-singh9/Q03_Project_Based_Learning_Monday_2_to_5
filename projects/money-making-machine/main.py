import streamlit as st
import random
import requests
import time
st.title("💸Money Making Machine")

def generate_money ():
    return random.randint(1,10000)
st.subheader("Instant Money Generating Machine 🙀")
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
            return ("freelacing")
    except:
        return ("Something went wrong")
    

st.subheader("Side Hustles Ideas🥱")
if st.button("Generate Hustles"):
    idea = fetch_side_hutles()
    st.info(idea)



def fetch_money_quotes ():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            money_quotes = response.json()
            return money_quotes
        else:
            return ("no money quotes avalaible")
    except:
        return ("no money quotes!")

st.subheader("Money Quotes 😶")
if st.button("Generate Money Quotes"):
    mq = fetch_money_quotes()
    st.info(mq)



