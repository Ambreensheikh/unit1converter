import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄")

# Custom CSS for colors
st.markdown(
    """
    <style>
    .stApp {
        background-color:rgb(143, 43, 143);  /* Lavender (Violet) */
    }
    
    .stButton {
        background-color: #9370DB;  /* Medium Purple */
        color: white;
    }
    .stTextInput, .stSelectbox {
        background-color:rgb(72, 181, 218);  /* Light Blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Unit Converter")

# Unit selection
unit_type = st.selectbox("Select unit type", ["Length", "Weight"])
if unit_type == "Length":
    units = ["Meters", "Kilometers", "Miles", "Feet"]
else:
    units = ["Grams", "Kilograms", "Pounds", "Ounces"]

# Input fields
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)
value = st.number_input("Value", min_value=0.0)

# Conversion logic
def convert_units(value, from_unit, to_unit):
    # Define conversion factors
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 1000,
        "Miles": 1609.34,
        "Feet": 0.3048,
        "Grams": 1,
        "Kilograms": 1000,
        "Pounds": 453.592,
        "Ounces": 28.3495
    }
    
    if unit_type == "Length":
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])
    else:
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Perform conversion
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")