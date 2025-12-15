from src.api.breach_checker import check_breach
import os
from dotenv import load_dotenv
from src.password_checker import check_strength
from src.password_generator import generate_password
from src.crypto_engine.encryptor import (
    hash_master_password,
    verify_master_password,
    generate_key,
    encrypt_data,
    decrypt_data,
)

load_dotenv()

VAULT_FILE = "data/vault.dat"


def initialize_vault():
    """Runs only on first use — sets master password + encryption key."""
    master_hash = os.getenv("MASTER_HASH")
    vault_key = os.getenv("VAULT_KEY")

    if master_hash and vault_key:
        return  # already set

    print("\n=== Vault Setup (First Time Only) ===")
    master = input("Create a master password: ")

    # hash and save master password
    hashed_pw = hash_master_password(master)
    key = generate_key()

    with open(".env", "w") as f:
        f.write(f"MASTER_HASH={hashed_pw.decode()}\n")
        f.write(f"VAULT_KEY={key.decode()}\n")

    print("Vault initialized successfully!")


def load_keys():
    master_hash = os.getenv("MASTER_HASH").encode()
    vault_key = os.getenv("VAULT_KEY").encode()
    return master_hash, vault_key


def unlock_vault(master_hash):
    master = input("Enter master password: ")
    if verify_master_password(master, master_hash):
        print("Vault unlocked!\n")
        return True
    else:
        print("Incorrect master password!")
        return False


def add_to_vault(key):
    site = input("Enter website/app name: ")
    pwd = input("Enter the password to save: ")

    token = encrypt_data(key, f"{site} : {pwd}")

    with open(VAULT_FILE, "ab") as f:
        f.write(token + b"\n")

    print("Saved securely!")


def view_vault(key):
    if not os.path.exists(VAULT_FILE):
        print("Vault empty.")
        return

    print("\n=== Stored Passwords (Decrypted) ===\n")

    with open(VAULT_FILE, "rb") as f:
        for line in f:
            try:
                decrypted = decrypt_data(key, line.strip())
                print(decrypted)
            except:
                print("[ERROR] Could not decrypt entry.")


def main():
    initialize_vault()
    master_hash, vault_key = load_keys()

    while True:
        print("\n=== SecurePass Vault – Version 2 ===")
        print("1. Check password strength")
        print("2. Generate secure password")
        print("3. Add password to encrypted vault")
        print("4. View saved passwords")
        print("5. Exit")
        print("6. Check Password breach (HIBP API)")

        choice = input("Enter your choice: ")

        if choice == "1":
            pwd = input("Enter password to analyze: ")
            result = check_strength(pwd)
            print(result)

        elif choice == "2":
            print("Generated:", generate_password())

        elif choice == "3":
            if unlock_vault(master_hash):
                add_to_vault(vault_key)

        elif choice == "4":
            if unlock_vault(master_hash):
                view_vault(vault_key)

        elif choice == "5":
            print("Goodbye!")
            break

        elif choice == "6":
            pwd = input("Enter password to check: ")
            count = check_breach(pwd)
            if count == 0:
                print("Password Not Leaked!!")
            else:
                print(f"Warring: Passowrd has been found {count} times in breaches!")
                
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
