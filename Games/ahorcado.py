from nltk.corpus import wordnet
import random

MAX_INTENTOS = 7

class Ahorcado:
    def __init__(self):
        self.intentos = 0
        self.palabra_secreta = self.obtener_palabra()
        self.palabra_oculta = self.ocultar_palabra(self.palabra_secreta)
        self.letras_incorrectas = []

    def jugar(self):
        print("Adivina la palabra secreta en español antes de ser ahorcado.")
        while self.intentos < MAX_INTENTOS:
            self.imprimir_estado_juego()
            letra_ingresada = self.pedir_letra()

            if letra_ingresada in self.palabra_secreta:
                self.actualizar_palabra_oculta(letra_ingresada)
            elif letra_ingresada not in self.letras_incorrectas:
                self.manipular_letra_incorrecta(letra_ingresada)

            if "_" not in self.palabra_oculta:
                self.mostrar_mensaje_final("¡Felicidades! La has adivinado.")
                break

        else:
            self.mostrar_mensaje_final("¡Lo siento! Te has quedado sin intentos.")

    def imprimir_estado_juego(self):
        print("Letras incorrectas: " + ", ".join(self.letras_incorrectas))
        mostrar_figura(self.intentos)
        print(self.palabra_oculta)

    def manipular_letra_incorrecta(self, letra):
        self.intentos += 1
        self.letras_incorrectas.append(letra)

    def obtener_palabra(self):
        palabras = [palabra for palabra in wordnet.all_lemma_names(pos='n', lang='spa') if "_" not in palabra]
        return random.choice(palabras).lower()

    def ocultar_palabra(self, palabra):
        return "_" * len(palabra)

    def pedir_letra(self):
        while True:
            texto_ingresado = input("Escriba una letra:\n").lower()
            if texto_ingresado.isalpha() and len(texto_ingresado) == 1:
                return texto_ingresado

    def actualizar_palabra_oculta(self, letra):
        nueva_palabra_oculta = ""
        for char, oculto_char in zip(self.palabra_secreta, self.palabra_oculta):
            nueva_palabra_oculta += char if char == letra else oculto_char
        self.palabra_oculta = nueva_palabra_oculta

    def mostrar_mensaje_final(self, mensaje):
        print(f"{mensaje} La palabra secreta era: {self.palabra_secreta}")

def mostrar_figura(intentos):
    figura = [
        '''
          +---+
          |   |
              |
              |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
              |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        ========'''
    ]
    print(figura[intentos])

if __name__ == "__main__":
    juego = Ahorcado()
    juego.jugar()
