import random
import string

print("======================================")
print("       RANDOM PASSWORD GENERATOR")
print("======================================")

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input(
            "Enter at least 2 choices separated by spaces (example: 1 2 3): "
        ).split()

        choices = list(dict.fromkeys(choices))

        if len(choices) < 2 or any(
            choice not in ["1", "2", "3", "4"] for choice in choices
        ):
            print("Error: Select at least 2 valid character types.")
            continue

        character_sets = {
            "1": string.ascii_uppercase,
            "2": string.ascii_lowercase,
            "3": string.digits,
            "4": string.punctuation
        }

        selected_characters = ""

        for choice in choices:
            selected_characters += character_sets[choice]

        password = ""

        # Add at least one character from each selected type
        for choice in choices:
            password += random.choice(character_sets[choice])

        remaining_length = length - len(password)

        for _ in range(remaining_length):
            password += random.choice(selected_characters)

        password_list = list(password)
        random.shuffle(password_list)
        password = "".join(password_list)

        print("\nGenerated Password:", password)

        again = input(
            "\nGenerate another password? (yes/no): "
        ).strip().lower()

        if again not in ["yes", "y"]:
            print("Goodbye!")
            break

    except ValueError:
        print("Error: Please enter a valid number for password length.")
