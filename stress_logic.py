# stress_logic.py
def calculate_stress(sleep_hours, work_hours, exercise_hours):
    """
    Simple logic to calculate stress score (0–100).
    Lower sleep, higher work, less exercise → higher stress.
    """

    stress_score = (10 - sleep_hours) * 5 + (work_hours * 3) - (exercise_hours * 2)

    # Keep score between 0 and 100
    stress_score = max(0, min(100, stress_score))

    # Categories
    if stress_score < 40:
        level = "Low"
    elif stress_score < 70:
        level = "Medium"
    else:
        level = "High"

    return level, stress_score
