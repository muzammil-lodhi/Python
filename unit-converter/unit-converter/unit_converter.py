import streamlit as st  # Import Streamlit for creating the web-based UI

# Function to convert units based on predefined conversion factors
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not found"

# Streamlit UI setup
st.title("📏 Unit Converter")

# User input
value = st.number_input("Enter the value:", min_value=1.0, step=1.0)

# Dropdowns for units
unit_from = st.selectbox("Convert From:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert To:", ["meter", "kilometer", "gram", "kilogram"])

# Conversion button
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: `{result}`")


