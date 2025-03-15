import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONE = [
   "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
   
]

st.title("Time Zone App")

selected_timezones = st.multiselect("Select Time Zone", TIME_ZONE, default=["UTC","Asia/Karachi"])
st.subheader("Selected Timezones")
for tz in selected_timezones:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")

    st.info(f"**{tz}** :{current_time}")

st.subheader("Convert Time between Tomezones")
current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONE, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONE, index=1)
if st.button("Convert Time"):

    dt  = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz)) 

    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")

    st.success(f"Converted Time: {to_tz}: {converted_time}")



