import random
import string


def generate_password(
    length: int = 16,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
) -> str:
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_special:
        pools.append("!@#$%^&*()-_=+[]{};:,.<>/?")

    if not pools:
        raise ValueError("At least one character type must be enabled.")

    all_chars = "".join(pools)

    # Guarantee at least one char from each selected pool
    password_chars = [random.choice(pool) for pool in pools]

    # Fill remaining length
    remaining = length - len(password_chars)
    password_chars += [random.choice(all_chars) for _ in range(remaining)]

    # Shuffle so the guaranteed characters aren't all at the front
    random.shuffle(password_chars)

    return "".join(password_chars)
