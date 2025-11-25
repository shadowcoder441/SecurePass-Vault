import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read key from .env
SECRET_KEY = os.getenv("SECRET_KEY")

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY is missing from .env file!")

# Convert string to bytes if necessary
if isinstance(SECRET_KEY, str):
    SECRET_KEY = SECRET_KEY.encode()

# Initialize Fernet object
cipher = Fernet(SECRET_KEY)


def encrypt_text(plain_text: str) -> bytes:
    """Encrypts a plain text string and returns encrypted bytes."""
    if not isinstance(plain_text, str):
        raise TypeError("encrypt_text expects a string input.")
    return cipher.encrypt(plain_text.encode())


def decrypt_text(token: bytes) -> str:
    """Decrypts encrypted bytes and returns the original string."""
    if not isinstance(token, (bytes, bytearray)):
        raise TypeError("decrypt_text expects bytes.")
    return cipher.decrypt(token).decode()
