import random
import string
from lorem_text import lorem

TEXT = "1"
PASSWORD = "2"

def generate_and_print_text():
    print("This tool will generate random text according to your preferences.")
    choice = verify_choice()
    required_text = generate_text(choice)
    print(required_text)

def verify_choice():
    while True:
        choice = input("Would you like to generate a text or a password?\n1. Text\n2. Password\nYour option: ")
        if choice in (TEXT, PASSWORD):
            return choice
        print("Invalid option. Write 1 for Text or 2 for password...")

def generate_text(choice):
    if choice == TEXT:
        length = ask_for_length()
        return generate_lorem_ipsum(length)
    else:
        default_option = input("Would you like to choose the default options? Y/N\n").upper() == "Y"
        return generate_random_text(default_option)

def generate_lorem_ipsum(length):
    return lorem.words(length)

def generate_random_text(default_option):
    length = ask_for_length()
    uppercase, lowercase, digits, special_chars = ask_for_options(default_option)
    characters = string.ascii_letters + string.digits + string.punctuation

    if not uppercase:
        characters = characters.translate(str.maketrans("", "", string.ascii_uppercase))
    if not lowercase:
        characters = characters.translate(str.maketrans("", "", string.ascii_lowercase))
    if not digits:
        characters = characters.translate(str.maketrans("", "", string.digits))
    if not special_chars:
        characters = characters.translate(str.maketrans("", "", string.punctuation))

    return ''.join(random.choices(characters, k=length))

def ask_for_length():
    while True:
        try:
            return int(input("What length do you prefer?\n"))
        except ValueError:
            print("Invalid number! Please type again...")

def ask_for_options(default_option):
    if default_option:
        return True, True, True, True

    uppercase = input("Do you want it capitalized? Y/N\n").upper() == "Y"
    lowercase = input("Should it include lowercase letters? Y/N\n").upper() == "Y"
    digits = input("Do you want it to include numbers? Y/N\n").upper() == "Y"
    special_chars = input("Should it include special characters? Y/N\n").upper() == "Y"

    return uppercase, lowercase, digits, special_chars

if __name__ == "__main__":
    generate_and_print_text()
