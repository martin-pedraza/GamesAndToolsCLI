import random

class AdivinaElNumero:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def jugar(self):
        print("Juego para adivinar número secreto entre 1 y 100 mediante preguntas de mayor o menor.")
        
        while True:
            numero_ingresado = self.obtener_numero_usuario()
            self.intentos += 1

            if self.verificar_adivinanza(numero_ingresado):
                break

    def obtener_numero_usuario(self):
        while True:
            try:
                return int(input("Ingrese un número: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def verificar_adivinanza(self, numero_ingresado):
        if numero_ingresado == self.numero_secreto:
            self.imprimir_mensaje_adivinaste()
            return True
        self.imprimir_mensaje_pista(numero_ingresado)
        return False

    def imprimir_mensaje_adivinaste(self):
        plural_intentos = "intentos" if self.intentos > 1 else "intento"
        print(f"Adivinaste!!! Adivinaste el número {self.numero_secreto} en {self.intentos} {plural_intentos}.")

    def imprimir_mensaje_pista(self, numero_ingresado):
        pista = "mayor" if self.numero_secreto > numero_ingresado else "menor"
        print(f"El número secreto es {pista}.")

if __name__ == "__main__":
    juego = AdivinaElNumero()
    juego.jugar()
