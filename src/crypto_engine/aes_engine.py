import os
from cryptography.fernet import Fernet, InvalidToken
from dotenv import load_dotenv

# Load variables from .env (SECRET_KEY)
load_dotenv()

def _load_key() -> bytes:
    """
    Load the SECRET_KEY from the environment (.env file).
    Raises a clear error if it's missing or invalid.
    """
    key = os.getenv("SECRET_KEY")
    if key is None:
        raise RuntimeError(
            "SECRET_KEY not found in environment. "
            "Make sure .env exists at project root with SECRET_KEY = b'...'"
        )

    # If stored as plain text, ensure it's bytes
    if isinstance(key, str):
        key = key.encode()

    try:
        # This will raise if key is the wrong length/format
        Fernet(key)
    except Exception as e:
        raise RuntimeError(f"SECRET_KEY in .env is invalid: {e}")

    return key


def _get_cipher() -> Fernet:
    """Return a Fernet cipher object using the loaded key."""
    key = _load_key()
    return Fernet(key)


def encrypt_text(plain_text: str) -> str:
    """
    Encrypt a string and return a *string* token (safe to store in JSON/DB).
    """
    if not isinstance(plain_text, str):
        raise TypeError("encrypt_text expects a string input.")

    cipher = _get_cipher()
    token: bytes = cipher.encrypt(plain_text.encode("utf-8"))
    # convert bytes -> string for storage
    return token.decode("utf-8")


def decrypt_text(token_str: str) -> str:
    """
    Decrypt a token string and return the original plaintext.
    """
    if not isinstance(token_str, str):
        raise TypeError("decrypt_text expects a string token.")

    cipher = _get_cipher()
    try:
        decrypted: bytes = cipher.decrypt(token_str.encode("utf-8"))
        return decrypted.decode("utf-8")
    except InvalidToken as e:
        # wrong key / corrupted data
        raise ValueError("Invalid encryption token or key.") from e
