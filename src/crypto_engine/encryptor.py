import bcrypt
from cryptography.fernet import Fernet


def hash_master_password(password: str) -> bytes:
    """Hash the master password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def verify_master_password(password: str, hashed: bytes) -> bool:
    """Verify the master password using bcrypt."""
    return bcrypt.checkpw(password.encode(), hashed)


def generate_key():
    """Generate a new Fernet key."""
    return Fernet.generate_key()


def encrypt_data(key: bytes, data: str) -> bytes:
    """Encrypt any string using Fernet."""
    f = Fernet(key)
    return f.encrypt(data.encode())


def decrypt_data(key: bytes, token: bytes) -> str:
    """Decrypt any Fernet token."""
    f = Fernet(key)
    return f.decrypt(token).decode()
