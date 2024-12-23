import streamlit as st
import joblib
import numpy as np

# Load the trained multi-linear regression model
model = joblib.load('multi_linear_regression.pkl')

# Title of the Streamlit app
st.title("Salary Prediction App")

# Description
st.write("""
This app predicts the salary of an individual based on:
- Age
- Years of Experience
""")

# Input fields for Age and Years of Experience
age = st.number_input("Enter Age:", min_value=18, max_value=65, value=25, step=1)
years_experience = st.number_input("Enter Years of Experience:", min_value=0.0, value=1.0, step=0.1)

# Predict button
if st.button("Predict Salary"):
    try:
        # Make prediction
        input_features = np.array([[age, years_experience]])
        predicted_salary = model.predict(input_features)
        st.success(f"Predicted Salary: ${predicted_salary[0]:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
