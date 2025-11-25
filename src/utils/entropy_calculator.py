import math
from collections import Counter


def calculate_entropy(password: str) -> float:
    """
    Shannon entropy in bits for the password.
    Higher = more unpredictable.
    """
    if not password:
        return 0.0

    counts = Counter(password)
    length = len(password)
    entropy = 0.0

    for count in counts.values():
        p = count / length
        entropy -= p * math.log2(p)

    # Entropy per character * total characters
    return round(entropy * length, 2)
