##################################
"""
Practice Python Scripts
Name Diceware Generator

Created by: Nowell Tiongco

History (latest on top):
2025-08-29  Initial Creation
"""
##################################

import random
import pandas as pd
import os

while True:
    try:
        number_of_names = int(input("Number of Names: "))
        break
    except ValueError:
        print("⚠️ Please enter a valid number.")

class NameDiceware:
    def __init__(self, number_of_names):
        self.number_of_names = number_of_names
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "names.csv")
        self.df = pd.read_csv(file_path)

    def define(self):
        print("Number of Names: ", self.number_of_names)

    def random_name(self):
        return random.choice(self.df.values.flatten().tolist())

    def generate_passphrase_kebab(self):
        """Generate passphrase with N random names joined by '-' """
        return "-".join(self.random_name() for _ in range(self.number_of_names))

# Create instance
generator = NameDiceware(number_of_names)

# Create passphrase in kebab-case
passphrase_kebab = generator.generate_passphrase_kebab()
print("kebab-case:", passphrase_kebab)

# Convert kebab-case to snake_case
passphrase_snake = passphrase_kebab.replace("-", "_")
print("snake_case:", passphrase_snake)

# Convert kebab-case to PascalCase
passphrase_pascal = "".join(word.capitalize() for word in passphrase_kebab.split("-"))
print("PascalCase:", passphrase_pascal)

# Convert kebab-case to camelCase
words = passphrase_kebab.split("-")
passphrase_camel = words[0] + "".join(word.capitalize() for word in words[1:])
print("camelCase:", passphrase_camel)

print()
input("Press Enter to exit...")