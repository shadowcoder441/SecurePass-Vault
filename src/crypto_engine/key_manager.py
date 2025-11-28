from pathlib import Path
import bcrypt

# Path where the hashed master password will be stored
MASTER_HASH_PATH = Path("data") / "master.passhash"


def master_password_is_set() -> bool:
    """Return True if a master password hash already exists."""
    return MASTER_HASH_PATH.exists()


def set_master_password(plain_password: str) -> None:
    """
    Hash and store the master password.
    Only call this when initializing the vault for the first time.
    """
    if not plain_password:
        raise ValueError("Master password cannot be empty.")

    MASTER_HASH_PATH.parent.mkdir(parents=True, exist_ok=True)

    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())
    MASTER_HASH_PATH.write_bytes(hashed)


def verify_master_password(plain_password: str) -> bool:
    """
    Check a given password against the stored hash.
    Returns True if correct, False otherwise.
    """
    if not master_password_is_set():
        # No master password yet
        return False

    stored_hash = MASTER_HASH_PATH.read_bytes()
    return bcrypt.checkpw(plain_password.encode("utf-8"), stored_hash)
