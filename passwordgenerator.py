import random
import string
import json

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length=12, complexity="medium"):
        characters = string.ascii_letters + string.digits
        if complexity == "high":
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated Password: {password}")
        return password

    def store_password(self, account, password):
        self.passwords[account] = password
        print(f"Password stored for account: {account}")

    def retrieve_password(self, account):
        if account in self.passwords:
            print(f"Password for {account}: {self.passwords[account]}")
        else:
            print(f"No password found for account: {account}")

    def save_to_file(self, filename="passwords.json"):
        with open(filename, "w") as file:
            json.dump(self.passwords, file)
        print(f"Passwords saved to {filename}")

    def load_from_file(self, filename="passwords.json"):
        try:
            with open(filename, "r") as file:
                self.passwords = json.load(file)
            print(f"Passwords loaded from {filename}")
        except FileNotFoundError:
            print(f"No saved passwords found in {filename}")

def main():
    manager = PasswordManager()
    manager.load_from_file()

    while True:
        print("\nPassword Generator and Manager")
        print("1. Generate Password")
        print("2. Store Password")
        print("3. Retrieve Password")
        print("4. Save Passwords to File")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            complexity = input("Choose complexity (low/medium/high): ").lower()
            manager.generate_password(length, complexity)
        elif choice == "2":
            account = input("Enter account name: ")
            password = input("Enter password to store: ")
            manager.store_password(account, password)
        elif choice == "3":
            account = input("Enter account name to retrieve: ")
            manager.retrieve_password(account)
        elif choice == "4":
            manager.save_to_file()
        elif choice == "5":
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
