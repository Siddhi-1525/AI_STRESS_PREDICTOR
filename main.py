# app.py
import streamlit as st
import matplotlib.pyplot as plt
from stress_logic import calculate_stress

# Title
st.title("🧠 AI Stress Predictor")

# User Inputs
sleep_hours = st.slider("Sleep Hours per Day", 0, 12, 7)
work_hours = st.slider("Work/Study Hours per Day", 0, 16, 8)
exercise_hours = st.slider("Exercise Hours per Day", 0, 5, 1)

# Button
if st.button("Predict Stress"):
    level, score = calculate_stress(sleep_hours, work_hours, exercise_hours)

    st.subheader(f"Predicted Stress Level: {level}")
    st.write(f"Stress Score: {score}/100")

    # Bar Plot
    categories = ["Low", "Medium", "High"]
    values = [0, 0, 0]

    if level == "Low":
        values[0] = score
    elif level == "Medium":
        values[1] = score
    else:
        values[2] = score

    fig, ax = plt.subplots()
    ax.bar(categories, values, color=['green', 'orange', 'red'])
    ax.set_ylabel("Score (0–100)")
    ax.set_title("Stress Prediction Result")

    st.pyplot(fig)
