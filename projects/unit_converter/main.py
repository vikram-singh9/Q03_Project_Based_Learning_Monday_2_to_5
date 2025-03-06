import streamlit as st # importing streamlit as st keyword

def convert_units(value, unit_from, unit_to):

    conversions = {
        "grams_kilograms" : 0.001,
        "kilograms_grams" : 1000,
        "meters_kilometers" : 0.001,
        "kilometers_meters": 1000,
        "grams_grams": 1,
        "kilograms_kilograms":1,
        "meters_meters":1,
        "kilometers_kilometers":1
    }

    # logic to create a units from and to
    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "conversion not supported." # esle statement if user selected wrong input
    

st.title("Unit Converter💛") # title of my app using built in streamlit function
    
value = st.number_input("Enter the Value: ", min_value=1.0, step=1.0) # user input 

unit_from = st.selectbox("Convert from", ["meters", "kilometers", "grams", "kilograms"]) # selecting from value 

unit_to = st.selectbox("Convert to", ["meters", "kilometers", "grams", "kilograms"]) # selecting to value

if st.button("Convert"): # button to trigger the function
    result = convert_units(value, unit_from, unit_to) # storing function in the variable
    st.write(f"Converted Units: {result}") # printing the converted unit OUTPUT
