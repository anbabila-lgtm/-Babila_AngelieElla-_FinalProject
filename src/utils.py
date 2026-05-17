"""
Utility functions for Password Vault
"""

import json
import os
import random
import string

DATA_PATH = "../data/passwords.json"

def ensure_data_file():

    os.makedirs(
        os.path.dirname(DATA_PATH),
        exist_ok=True
    )

    if not os.path.exists(DATA_PATH):

        initial_data = {
            "passwords": []
        }

        save_data(initial_data)

def save_data(data):

    with open(DATA_PATH, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

def load_data():

    ensure_data_file()

    try:

        with open(DATA_PATH, "r") as file:

            return json.load(file)

    except json.JSONDecodeError:

        print("⚠️ Error reading JSON file!")

        return {"passwords": []}

def get_valid_input(
    prompt,
    input_type=str,
    valid_options=None
):

    while True:

        try:

            value = input_type(input(prompt))

            if valid_options and value not in valid_options:

                print(
                    f"Choose only from {valid_options}"
                )

                continue

            return value

        except ValueError:

            print(
                f"Please enter valid {input_type.__name__}"
            )

def generate_password(length):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    return password

def check_password_strength(password):

    score = 0

    # Set example
    special_chars = set("!@#$%^&*()")

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in special_chars for char in password):
        score += 1

    strengths = (
        "Weak",
        "Medium",
        "Strong",
        "Very Strong"
    )

    return strengths[score - 1] if score > 0 else "Weak"
