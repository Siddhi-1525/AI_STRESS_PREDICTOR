# app.py
import streamlit as st
import matplotlib.pyplot as plt
from stress_logic import calculate_stress

# Page config
st.set_page_config(page_title="AI Stress Predictor", page_icon="🧠", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 AI Stress Predictor</h1>", unsafe_allow_html=True)
st.write("Check your stress level with lifestyle inputs and get professional suggestions.")

# Sidebar Inputs
st.sidebar.header("⚙️ Lifestyle Inputs")
sleep_hours = st.sidebar.slider("😴 Sleep Hours per Day", 0, 12, 7)
work_hours = st.sidebar.slider("💻 Work/Study Hours per Day", 0, 16, 8)
exercise_hours = st.sidebar.slider("🏃 Exercise Hours per Day", 0, 5, 1)
diet_quality = st.sidebar.slider("🍔 Diet Quality (1=Poor, 5=Excellent)", 1, 5, 3)
screen_time = st.sidebar.slider("📱 Screen Time (hours/day)", 0, 12, 6)
caffeine = st.sidebar.slider("☕ Caffeine Intake (cups/day)", 0, 10, 2)
self_stress = st.sidebar.slider("🤯 Self-Reported Stress (1–10)", 1, 10, 5)

# Button
if st.button("🔮 Predict Stress"):
    level, score, suggestions = calculate_stress(
        sleep_hours, work_hours, exercise_hours,
        diet_quality, screen_time, caffeine, self_stress
    )

    # Results
    st.subheader(f"✅ Predicted Stress Level: **{level}**")
    st.progress(score)
    st.write(f"**Stress Score:** {score}/100")

    # ----------- SINGLE PROFESSIONAL BAR GRAPH -----------
    categories = ["Sleep", "Work", "Exercise", "Diet", "Screen", "Caffeine", "Self-Stress"]
    values = [sleep_hours, work_hours, exercise_hours, diet_quality, screen_time, caffeine, self_stress]

    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(categories, values, color="#4CAF50", edgecolor="black")

    # Add values above bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, str(yval),
                ha="center", va="bottom", fontsize=10, fontweight="bold")

    ax.set_ylabel("Input Values", fontsize=12)
    ax.set_title("📊 Lifestyle Factors Overview", fontsize=14, fontweight="bold")
    st.pyplot(fig)

    # ----------- REMEDIES / CONSISTENCY TIPS -----------
    st.write("### 🩺 Recommendations")
    for tip in suggestions:
        st.write(f"- {tip}")
