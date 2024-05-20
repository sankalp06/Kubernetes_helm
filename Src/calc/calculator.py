import streamlit as st
import requests

st.title("Adder and Subtractor Service")

# Input fields
a = st.number_input("Enter the value for a", value=0.0)
b = st.number_input("Enter the value for b", value=0.0)

# Create columns for buttons
col1, col2 = st.columns(2)

# Add button and response display
with col1:
    if st.button("Add"):
        try:
            # Communicate with Adder Service
            adder_response = requests.get(f"http://host.docker.internal:5001", params={'a': a, 'b': b})
            adder_response.raise_for_status()  # Raise an error for bad responses
            adder_data = adder_response.json()
            print(adder_data)
            sum_result = adder_data.get('sum')

            if sum_result is None:
                st.error("Invalid response from Adder service.")
            else:
                st.write(f"Sum: {sum_result}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while making the request: {e}")
        except ValueError as e:
            st.error(f"JSON decoding failed: {e}")

# Subtract button and response display
with col2:
    if st.button("Subtract"):
        try:
            # Communicate with Subtractor Service
            subtractor_response = requests.get(f"http://host.docker.internal:5002", params={'a': a, 'b': b})
            subtractor_response.raise_for_status()  # Raise an error for bad responses
            subtractor_data = subtractor_response.json()
            print(subtractor_data)
            difference_result = subtractor_data.get('sum')

            if difference_result is None:
                st.error("Invalid response from Subtractor service.")
            else:
                st.write(f"Difference: {difference_result}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while making the request: {e}")
        except ValueError as e:
            st.error(f"JSON decoding failed: {e}")
