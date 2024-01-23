import random
import string

def generate_and_print_text():
    print("This tool will generate random text according to your preferences.")
    default_option = input("Would you like to choose the default options? Y/N\n").upper() == "Y"
    print(generate_random_text() if default_option else generate_custom_text())

def generate_custom_text():
    length = ask_for_length()
    options = ask_for_options()
    return generate_random_text(length, **options)

def generate_random_text(length=8, **options):
    characters = ""

    if options.get('uppercase', False):
        characters += string.ascii_uppercase
    if options.get('lowercase', False):
        characters += string.ascii_lowercase
    if options.get('digits', False):
        characters += string.digits
    if options.get('special_chars', False):
        characters += string.punctuation
    if options.get('whitespace', False):
        characters += string.whitespace

    if not characters:
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    return ''.join(random.sample(characters, length))

def ask_for_length():
    while True:
        try:
            return int(input("What length do you prefer?\n"))
        except ValueError:
            print("Invalid number! Type again, please...")

def ask_for_options():
    uppercase = input("Do you want it capitalized? Y/N\n").upper() == "Y"
    lowercase = input("Should it include lowercase letters? Y/N\n").upper() == "Y"
    digits = input("Do you want it to include numbers? Y/N\n").upper() == "Y"
    special_chars = input("Should it include special characters? Y/N\n").upper() == "Y"
    whitespace = input("Do you want it to include whitespaces? Y/N\n").upper() == "Y"

    return {
        'uppercase': uppercase,
        'lowercase': lowercase,
        'digits': digits,
        'special_chars': special_chars,
        'whitespace': whitespace,
    }

if __name__ == "__main__":
    generate_and_print_text()
