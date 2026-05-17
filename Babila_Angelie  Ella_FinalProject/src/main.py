"""
CLI Password Vault Manager
"""

import os
from utils import (
    load_data,
    save_data,
    get_valid_input,
    generate_password,
    check_password_strength
)

from models import PasswordEntry

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():

    while True:

        clear_screen()

        print("=" * 45)
        print("🔐 PASSWORD VAULT MANAGER".center(45))
        print("=" * 45)

        print("1. Add New Password")
        print("2. View Saved Accounts")
        print("3. Search Account")
        print("4. Delete Account")
        print("5. Generate Strong Password")
        print("6. Exit")

        choice = get_valid_input(
            "Enter choice: ",
            int,
            [1,2,3,4,5,6]
        )

        if choice == 1:
            add_password()

        elif choice == 2:
            view_accounts()

        elif choice == 3:
            search_account()

        elif choice == 4:
            delete_account()

        elif choice == 5:
            generate_new_password()

        elif choice == 6:
            print("\n✅ Password vault saved!")
            break

def add_password():

    data = load_data()

    website = input("Website/App: ")
    username = input("Username/Email: ")
    password = input("Password: ")

    strength = check_password_strength(password)

    entry = PasswordEntry(
        website,
        username,
        password,
        strength
    )

    data["passwords"].append(entry.to_dict())

    save_data(data)

    print(f"✅ Password saved! Strength: {strength}")

    input("\nPress Enter to continue...")


def view_accounts():

    data = load_data()

    if not data["passwords"]:
        print("No saved accounts!")
        return

    print("\n🔑 SAVED ACCOUNTS\n")

    for i, acc in enumerate(data["passwords"], 1):

        print(f"{i}. {acc['website']}")
        print(f"   Username: {acc['username']}")
        print(f"   Password: {acc['password']}")
        print(f"   Strength: {acc['strength']}")
        print(f"   Date Added: {acc['date_added']}\n")
    input("\nPress Enter to return to menu...") 

def search_account():

    data = load_data()

    keyword = input("Search website/app: ").lower()

    found = [
        acc for acc in data["passwords"]
        if keyword in acc["website"].lower()
    ]

    if not found:
        print("No matching account found!")
        input("\nPress Enter to continue...")
        return

    print("\n🔎 SEARCH RESULTS\n")

    for acc in found:

        print(f"Website: {acc['website']}")
        print(f"Username: {acc['username']}")
        print(f"Password: {acc['password']}\n")

    input("\nPress Enter to continue...")
 
def delete_account():

    data = load_data()

    if not data["passwords"]:
        print("No accounts to delete!")
        input("\nPress Enter to continue...")
        return

    for i, acc in enumerate(data["passwords"], 1):
        print(f"{i}. {acc['website']}")

    idx = get_valid_input(
        "Enter account number: ",
        int
    ) - 1

    if 0 <= idx < len(data["passwords"]):

        del data["passwords"][idx]

        save_data(data)

        print("✅ Account deleted!")

        input("\nPress Enter to continue...")

def generate_new_password():

    length = get_valid_input(
        "Password length: ",
        int
    )

    password = generate_password(length)

    print(f"\n🔐 Generated Password: {password}")

    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
