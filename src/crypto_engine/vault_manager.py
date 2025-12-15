import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

from .aes_engine import encrypt_text, decrypt_text

VAULT_PATH = Path("data") / "password_vault.json"


def _load_vault() -> Dict:
    """
    Load the vault JSON file. If it doesn't exist, return an empty structure.
    Structure:
    {
        "entries": [
            {
                "id": 1,
                "service": "...",
                "username": "...",
                "password_enc": "...",   # encrypted string
                "created_at": "...",
                "updated_at": "..."
            },
            ...
        ]
    }
    """
    if not VAULT_PATH.exists():
        return {"entries": []}

    with VAULT_PATH.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Corrupted file fallback
            return {"entries": []}


def _save_vault(vault: Dict) -> None:
    """Save the vault structure back to disk."""
    VAULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with VAULT_PATH.open("w", encoding="utf-8") as f:
        json.dump(vault, f, indent=2)


def list_entries() -> List[Dict]:
    """
    Return a list of entries WITHOUT decrypting passwords.
    (Good for showing a table of services/usernames.)
    """
    vault = _load_vault()
    return vault.get("entries", [])


def add_entry(service: str, username: str, plain_password: str) -> Dict:
    """
    Add a new encrypted entry to the vault.
    Returns the created entry (without decrypting).
    """
    vault = _load_vault()
    entries = vault.setdefault("entries", [])

    new_id = (max((e["id"] for e in entries), default=0) + 1) if entries else 1

    now = datetime.utcnow().isoformat()

    encrypted = encrypt_text(plain_password)

    entry = {
        "id": new_id,
        "service": service,
        "username": username,
        "password_enc": encrypted,
        "created_at": now,
        "updated_at": now,
    }

    entries.append(entry)
    _save_vault(vault)
    return entry


def get_entry_decrypted(entry_id: int) -> Optional[Dict]:
    """
    Return a single entry with the password DECRYPTED.
    If not found, returns None.
    """
    vault = _load_vault()
    for e in vault.get("entries", []):
        if e["id"] == entry_id:
            decrypted_pw = decrypt_text(e["password_enc"])
            result = dict(e)
            result["password_plain"] = decrypted_pw
            return result
    return None


def delete_entry(entry_id: int) -> bool:
    """
    Delete an entry by id. Returns True if deleted, False if not found.
    """
    vault = _load_vault()
    entries = vault.get("entries", [])
    new_entries = [e for e in entries if e["id"] != entry_id]

    if len(new_entries) == len(entries):
        return False  # nothing deleted

    vault["entries"] = new_entries
    _save_vault(vault)
    return True
