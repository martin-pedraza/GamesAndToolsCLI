from nltk.corpus import wordnet
from googletrans import Translator

def translate_and_find_definition():
    word = ask_for_word()
    definition = get_word_definition(word)
    if definition:
        show_definition_word(definition)
        translation = translate_to_spanish(word)
        show_translation(translation)
    else:
        show_no_definition()

def ask_for_word():
    while True:
        word = input("Please enter a word (only letters): ").strip()
        if verify_word(word):
            return word
        print("Invalid input. Please enter a valid word.")

def verify_word(word):
    return word.isalpha() and len(word) >= 1

def get_word_definition(word):
    synsets = wordnet.synsets(word)
    return synsets[0].definition() if synsets else None

def show_no_definition():
    print("No definition was found for the word")

def show_definition_word(definition):
    print(f"Definition: {definition}")

def translate_to_spanish(word):
    translator = Translator()
    translation = translator.translate(word, src='en', dest='es')
    return translation.text

def show_translation(translation):
    print(f"Spanish translation: {translation}")
    
if __name__ == "__main__":
    translate_and_find_definition()