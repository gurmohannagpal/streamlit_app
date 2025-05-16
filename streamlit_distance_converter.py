import streamlit as st

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

st.title("Distance Converter: Kilometers  Miles")

conversion_type = st.radio(
    "Choose conversion direction:",
    ("Kilometers to Miles", "Miles to Kilometers")
)

if conversion_type == "Kilometers to Miles":
    km = st.number_input("Enter distance in kilometers:", min_value=0.0, format="%.3f")
    if st.button("Convert"):
        miles = km_to_miles(km)
        st.success(f"{km} kilometers = {miles:.3f} miles")
else:
    miles = st.number_input("Enter distance in miles:", min_value=0.0, format="%.3f")
    if st.button("Convert"):
        km = miles_to_km(miles)
        st.success(f"{miles} miles = {km:.3f} kilometers")
