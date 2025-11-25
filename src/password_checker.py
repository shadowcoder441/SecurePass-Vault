from .utils.entropy_calculator import calculate_entropy
from .utils.validator import is_common_password


def check_strength(password: str) -> dict:
    feedback = []
    score = 0

    # -------- LENGTH SCORING (max 4) --------
    length = len(password)
    if length >= 20:
        score += 4
    elif length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # -------- CHARACTER CLASS SCORING (max 4) --------
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_chars = "!@#$%^&*()-_=+[]{};:,.<>/?"
    has_special = any(c in special_chars for c in password)

    class_score = sum([has_lower, has_upper, has_digit, has_special])
    score += class_score   # max 4

    if not has_lower:
        feedback.append("Add lowercase letters.")
    if not has_upper:
        feedback.append("Add uppercase letters.")
    if not has_digit:
        feedback.append("Add digits.")
    if not has_special:
        feedback.append("Add special characters (!,@,#, etc).")

    # -------- COMMON PASSWORD CHECK (penalty) --------
    if is_common_password(password):
        feedback.append("This password appears in common-password lists.")
        score -= 2

    # -------- ENTROPY SCORING (max 2) --------
    entropy_bits = calculate_entropy(password)

    if entropy_bits >= 70:
        score += 2
    elif entropy_bits >= 55:
        score += 1
    else:
        feedback.append("Entropy is low; consider a longer password.")

    # -------- CAP BETWEEN 0 AND 10 --------
    score = max(0, min(score, 10))

    # -------- LABEL --------
    if score <= 3:
        label = "Very Weak"
    elif score <= 5:
        label = "Weak"
    elif score <= 7:
        label = "Moderate"
    elif score <= 9:
        label = "Strong"
    else:
        label = "Very Strong"

    return {
        "score": score,
        "label": label,
        "entropy_bits": entropy_bits,
        "feedback": feedback,
    }
