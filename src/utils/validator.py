_COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "iloveyou",
    "admin",
    "welcome",
    "letmein",
    "abc123",
    "111111",
    "123123",
    "password1",
}

def is_common_password(password: str) -> bool:
    return password.lower() in _COMMON_PASSWORDS
