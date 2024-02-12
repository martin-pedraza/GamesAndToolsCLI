import os
import time

# Constantes para las opciones del menú
GAMES = 1
TOOLS = 2
LANGUAGE = 3
EXIT = 4

# Diccionario de mensajes de bienvenida
WELCOME_MESSAGES = {
    "en": "Welcome to Games and Tools CLI!",
    "es": "¡Bienvenido a los Juegos y Herramientas CLI!"
}

# Diccionario de opciones de menú
MENU_OPTIONS = {
    "en": ["1. Play Games (Spanish)", "2. Use Tools (English)", "3. Change language", "4. Exit"],
    "es": ["1. Jugar Juegos (Español)", "2. Usar herramientas (Inglés)", "3. Cambiar idioma", "4. Salir"]
}

# Diccionario de títulos de menú
MENU_TITLES = {
    "en": {"games": "Games Menu:", "tools": "Tools Menu:"},
    "es": {"games": "Menú Juegos:", "tools": "Menú Herramientas:"}
}

# Diccionario de opciones de juegos y herramientas
MENU_OPTIONS_DETAILS = {
    "games": ["Guess the Number", "Hangman", "Blackjack", "Higher or Lower", "Tic-Tac-Toe"],
    "tools": ["Code Generator", "PDF Converter", "Text Generator", "Translating Dictionary", "Windows Optimizer"]
}

def start_cli():
    language = "en"
    while True:
        time.sleep(3)
        clear_console()
        show_intro(language)
        choice = get_choice([GAMES, TOOLS, LANGUAGE, EXIT], language)
        if choice == LANGUAGE:
            language = toggle_language(language)
        elif choice == GAMES:
            play_game(language)
        elif choice == TOOLS:
            use_tool(language)
        elif choice == EXIT:
            return

def show_intro(language):
    print(WELCOME_MESSAGES[language])
    print("Please choose an option:" if language == "en" else "Por favor elige una opción:")
    for option in MENU_OPTIONS[language]:
        print(option)

def get_choice(options, language):
    while True:
        try:
            choice = int(input("Enter your choice: " if language == "en" else "Ingrese su elección: "))
            if choice in options:
                return choice
        except ValueError:
            pass
        print("Invalid option..." if language == "en" else "Opción no válida...")

def toggle_language(language):
    return "en" if language == "es" else "es"

def play_game(language):
    show_submenu("games", language)
    game_choice = get_choice(range(1, 6), language)
    open_game(game_choice)

def use_tool(language):
    show_submenu("tools", language)
    tool_choice = get_choice(range(1, 6), language)
    open_tool(tool_choice)

def show_submenu(menu_type, language):
    print(MENU_TITLES[language][menu_type])
    for i, option in enumerate(MENU_OPTIONS_DETAILS[menu_type], start=1):
        print(f"{i}. {option}")

def open_game(game_choice):
    game_files = ["adivina_el_numero.py", "ahorcado.py", "blackjack.py", "mayor_o_menor.py", "ta_te_ti.py"]
    game_filename = f"Games/{game_files[game_choice - 1]}"
    if os.path.isfile(game_filename):
        os.system(f"python {game_filename}")

def open_tool(tool_choice):
    tool_files = ["code_generator.py", "pdf_converter.py", "text_generator.py", "translating_dictionary.py", "windows_optimizer.py"]
    tool_filename = f"Tools/{tool_files[tool_choice - 1]}"
    if os.path.isfile(tool_filename):
        os.system(f"python {tool_filename}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    start_cli()
