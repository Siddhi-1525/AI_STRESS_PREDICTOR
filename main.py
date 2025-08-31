# app.py
import streamlit as st
import matplotlib.pyplot as plt
from stress_logic import calculate_stress, give_advice

# Page config
st.set_page_config(page_title="AI Stress Predictor", page_icon="📊", layout="centered")

st.title("📊 AI Stress Level Predictor - Student Edition")
st.write("Enter your details below to check your stress level:")

# Inputs
sleep = st.number_input("🛌 Daily Sleep Hours", min_value=0, max_value=24, step=1)
study = st.number_input("📖 Daily Study Hours", min_value=0, max_value=24, step=1)
pending = st.number_input("📚 Pending Subjects", min_value=0, max_value=10, step=1)

# Storage for history
if "history" not in st.session_state:
    st.session_state.history = []

# Predict button
if st.button("Predict Stress"):
    level, score = calculate_stress(sleep, study, pending)
    advice = give_advice(level)

    st.success(f"### Stress Level: {level}\n**Score:** {score}\n💡 {advice}")

    st.session_state.history.append(score)

# Show Graph
if st.button("Show Graph"):
    if st.session_state.history:
        fig, ax = plt.subplots()
        ax.plot(st.session_state.history, marker="o")
        ax.set_title("Stress Trend Over Time")
        ax.set_xlabel("Prediction Attempts")
        ax.set_ylabel("Stress Score")
        st.pyplot(fig)
    else:
        st.warning("No data yet. Predict stress multiple times first.")
