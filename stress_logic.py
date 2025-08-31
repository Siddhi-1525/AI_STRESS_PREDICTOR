# stress_logic.py

def calculate_stress(sleep_hours, study_hours, pending_subjects):
    score = 0

    # Sleep factor
    if sleep_hours < 6:
        score += 2
    elif 6 <= sleep_hours < 8:
        score += 1

    # Study factor
    if study_hours > 8:
        score += 2
    elif 5 <= study_hours <= 8:
        score += 1

    # Pending subjects factor
    if pending_subjects >= 5:
        score += 2
    elif 2 <= pending_subjects < 5:
        score += 1

    # Stress Level
    if score <= 2:
        level = "LOW"
    elif 3 <= score <= 4:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return level, score


def give_advice(level):
    if level == "LOW":
        return "Great! Keep balancing sleep, study and relaxation. 🌸"
    elif level == "MEDIUM":
        return "You’re doing okay. Try sleeping 7-8 hours and revise with Pomodoro technique. ⏳"
    else:
        return "⚠️ You're stressed! Sleep more, take breaks, and divide subjects into small goals. 💡"
