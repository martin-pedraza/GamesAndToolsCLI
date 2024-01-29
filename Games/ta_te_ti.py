import random
import os
import time

class Tateti():
    TRIUNFO = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [1, 4, 7],
               [2, 5, 8],
               [3, 6, 9],
               [1, 5, 9],
               [3, 5, 7]
               ]
    CRUZ = "X"
    CIRCULO = "O"

    def __init__(self):
        self.opciones = list(range(1, 10))
        self.elecciones = ["-" for _ in range(9)]
        self.turno_humano = True

    def jugar(self):
        while sum(self.opciones) != 0:
            self.jugar_turno()
            if self.verificar_triunfo() != (False, None):
                break
            self.turno_humano = not self.turno_humano
            time.sleep(3)
            self.limpiar_consola()
        else:
            print("Has empatado...")
            return
        self.mostrar_mensaje_final()
    
    def jugar_turno(self):
        if self.turno_humano:
            self.mostrar_tablero(True)
            opcion = self.elegir_opcion()
        else:
            print("Turno del oponente...")
            opcion = self.cambiar_a_oponente()
        self.actualizar_tablero(opcion)
        self.mostrar_tablero()

    def actualizar_tablero(self, opcion):
        self.opciones[opcion - 1] = 0
        self.elecciones[opcion - 1] = self.CRUZ if self.turno_humano else self.CIRCULO
    
    def mostrar_tablero(self, mostrar_opcion=False):
        celdas = [str(celda) if celda != "-" else str(opcion if mostrar_opcion else " ") for celda, opcion in zip(self.elecciones, self.opciones)]
        filas = [f" {celdas[i]} | {celdas[i + 1]} | {celdas[i + 2]} " for i in range(0, 9, 3)]
        tablero = "\n---|---|---\n".join(filas)
        print(tablero)
    
    def elegir_opcion(self):
        while True:
            try:
                opcion = int(input("Elige la opción: "))
                if opcion in self.opciones:
                    return opcion
            except ValueError:
                pass
            print("Elige una opción válida...")

    def cambiar_a_oponente(self):
        opcion = random.choice(self.opciones)
        while opcion == 0:
            opcion = random.choice(self.opciones)
        return opcion
    
    def verificar_triunfo(self):
        for triunfo in self.TRIUNFO:
            if all(self.elecciones[i - 1] == self.CRUZ for i in triunfo):
                return True, self.CRUZ
            elif all(self.elecciones[i - 1] == self.CIRCULO for i in triunfo):
                return True, self.CIRCULO
        return False, None
    
    def mostrar_mensaje_final(self):
        mensaje = "Has ganado!!!" if self.verificar_triunfo() == (True, self.CRUZ) else "Has perdido..."
        print(mensaje)

    @staticmethod
    def limpiar_consola():
        os.system('cls' if os.name == 'nt' else 'clear')
    
if __name__ == "__main__":
    juego = Tateti()
    juego.jugar()