import hashlib
import requests

HIBP_API = "https://api.pwnedpasswords.com/range/"


def check_breach(password: str) -> int:
    """
    Returns number of times the password appears in breaches.
    Uses K-Anonymity (only first 5 chars of SHA1 hash is sent).
    """
    if not password:
        return -1

    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # Request only the hash range that shares the same prefix
    response = requests.get(HIBP_API + prefix)
    if response.status_code != 200:
        raise RuntimeError("Error reaching HIBP API")

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)  # number of breaches

    return 0
