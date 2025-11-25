from src.password_checker import check_strength
from src.password_generator import generate_password


def print_menu():
    print("\n=== SecurePass Vault – v1 (CLI) ===")
    print("1. Check password strength")
    print("2. Generate a secure password")
    print("3. Exit")


def handle_check_password():
    pwd = input("\nEnter the password to analyze: ")
    result = check_strength(pwd)

    print(f"\nScore   : {result['score']}/10")
    print(f"Rating  : {result['label']}")
    print(f"Entropy : {result['entropy_bits']} bits")

    if result["feedback"]:
        print("\nSuggestions:")
        for line in result["feedback"]:
            print(f"  - {line}")
    else:
        print("\nLooks solid. No immediate issues found.")


def handle_generate_password():
    try:
        length_str = input("\nDesired length (recommend 10–20): ")
        length = int(length_str)
    except ValueError:
        print("Invalid length. Please enter a number.")
        return

    pwd = generate_password(length=length)
    print("\nGenerated password:")
    print(pwd)
    print("\nReminder: Use a password manager instead of memorising this.")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            handle_check_password()
        elif choice == "2":
            handle_generate_password()
        elif choice == "3":
            print("\nExiting SecurePass Vault. Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
