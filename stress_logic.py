# stress_logic.py

def calculate_stress(sleep, work, exercise, diet, screen, caffeine, self_stress):
    """
    Calculate stress score (0–100) and level based on lifestyle factors.
    Returns (level, score, suggestions).
    """

    score = 0

    # Sleep
    if sleep < 6:
        score += 20
    elif sleep > 9:
        score += 5

    # Work/Study hours
    if work > 10:
        score += 20
    elif work < 4:
        score += 5

    # Exercise
    if exercise < 1:
        score += 15
    elif exercise >= 2:
        score -= 5

    # Diet (1=poor, 5=excellent)
    score += (6 - diet) * 3  

    # Screen time
    if screen > 8:
        score += 15
    elif screen < 4:
        score -= 5

    # Caffeine
    if caffeine > 4:
        score += 10

    # Self-reported stress
    score += self_stress * 5

    # Clamp score
    score = min(max(score, 0), 100)

    # Stress level + suggestions
    if score < 35:
        level = "Low"
        suggestions = [
            "Maintain regular sleep of 7–8 hours.",
            "Keep exercising at least 3–4 times a week.",
            "Balance screen time with offline activities.",
            "Continue mindful practices like meditation or journaling."
        ]
    elif score < 70:
        level = "Medium"
        suggestions = [
            "Improve diet: add fruits, vegetables, and hydration.",
            "Take short breaks between long work/study sessions.",
            "Reduce caffeine and increase physical activity.",
            "Practice relaxation (deep breathing, yoga, meditation)."
        ]
    else:
        level = "High"
        suggestions = [
            "Prioritize sleep and cut down late-night screen time.",
            "Seek support from friends, family, or a counselor.",
            "Reduce workload or break tasks into smaller parts.",
            "Adopt stress-relieving habits like daily walks or mindfulness."
        ]

    return level, score, suggestions
