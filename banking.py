import json

# File to store account details
DATA_FILE = "accounts.json"

# Load account data
def load_accounts():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save account data
def save_accounts(accounts):
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

# Deposit function
def deposit(account_number, amount):
    if amount > 0:
        accounts[account_number] += amount
        save_accounts(accounts)
        print(f"Deposit successful. New balance: {accounts[account_number]}")
    else:
        print("Invalid amount. Please enter a positive value.")

# Withdraw function
def withdraw(account_number, amount):
    if 0 < amount <= accounts[account_number]:
        accounts[account_number] -= amount
        save_accounts(accounts)
        print(f"Withdrawal successful. New balance: {accounts[account_number]}")
    else:
        print("Insufficient funds or invalid amount.")

# Check balance function
def check_balance(account_number):
    print(f"Current balance: {accounts[account_number]}")

# Main function
accounts = load_accounts()
account_number = input("Enter your account number: ")

if account_number not in accounts:
    print("Account not found.")
else:
    while True:
        choice = input("Choose an option: deposit, withdraw, balance, exit: ").lower()
        if choice == "deposit":
            deposit(account_number, float(input("Enter amount: ")))
        elif choice == "withdraw":
            withdraw(account_number, float(input("Enter amount: ")))
        elif choice == "balance":
            check_balance(account_number)
        elif choice == "exit":
            print("Thank you for using the banking system!")
            break
