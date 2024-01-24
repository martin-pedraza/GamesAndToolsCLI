import random
import time

class Blackjack():
    MAX_PUNTOS = 21
    TIEMPO_ESPERA = 3

    def __init__(self):
        self.suma = 0
        self.cartas = []
        self.suma_final = 0

    def jugar(self):
        print("Obten cartas, suma hasta 21 sin pasarte, gana quien esté más cerca.")
        self.iniciar_juego()
        self.jugar_rondas()
        self.mostrar_resultado_final()

    def iniciar_juego(self):
        for _ in range(2):
            self.repartir_ronda()

    def jugar_rondas(self):
        while self.preguntar_otra_carta():
            self.repartir_ronda()
            if not self.verificar_suma():
                print("Has perdido...")
                return
        else:
            self.reiniciar_valores()

        print("El turno de tu oponente")
        while self.suma < self.suma_final and self.verificar_suma():
            self.repartir_ronda()

    def mostrar_resultado_final(self):
        resultado = self.obtener_resultado()
        print(f"{resultado} Tu puntos fueron {self.suma_final} y tu oponente hizo {self.suma}.")

    def obtener_resultado(self):
        if self.suma_final > self.suma or not self.verificar_suma():
            return "Ganaste!!!"
        elif self.suma_final < self.suma:
            return "Perdiste!"
        else:
            return "Empataste..."
            
    def repartir_ronda(self):
        time.sleep(self.TIEMPO_ESPERA)
        self.agregar_carta()
        self.mostrar_estado_actual()

    def agregar_carta(self):
        carta = self.generar_carta()
        self.cartas.append(carta)
    
    def mostrar_estado_actual(self):
        self.mostrar_carta_actual()
        self.calcular_suma()
        self.mostrar_suma()

    def generar_carta(self):
        return random.randint(1, 13)
    
    def calcular_suma(self):
        carta = self.cartas[-1]
        if self.suma < 11 and carta == 1:
            self.suma += 11
        elif self.suma > 11 and carta == 1:
            self.suma += 1
        elif carta in (11, 12, 13):
            self.suma += 10
        else:
            self.suma += carta

    def verificar_suma(self):
        return self.suma < self.MAX_PUNTOS
    
    def mostrar_suma(self):
        print(f"La suma es: {self.suma}")

    def preguntar_otra_carta(self):
        while True:
            texto_ingresado = input("Quieres otra carta? S/N\n").lower()
            if texto_ingresado in ('s', 'n'):
                return texto_ingresado == 's'
            print("No es una respuesta válida...")

    def reiniciar_valores(self):
        self.suma_final = self.suma
        self.suma = 0
        self.cartas = []

    def mostrar_carta(self, carta):
        print(carta)

    def mostrar_carta_actual(self):
        figuras_cartas = [            
            '''
             .----------------. 
            | .--------------. |
            | |      __      | |
            | |     /  \     | |
            | |    / /\ \    | |
            | |   / ____ \   | |
            | | _/ /    \ \_ | |
            | ||____|  |____|| |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |    _____     | |
            | |   / ___ `.   | |
            | |  |_/___) |   | |
            | |   .'____.'   | |
            | |  / /____     | |
            | |  |_______|   | |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |    ______    | |
            | |   / ____ `.  | |
            | |   `'  __) |  | |
            | |   _  |__ '.  | |
            | |  | \____) |  | |
            | |   \______.'  | |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |   _    _     | |
            | |  | |  | |    | |
            | |  | |__| |_   | |
            | |  |____   _|  | |
            | |      _| |_   | |
            | |     |_____|  | |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |   _______    | |
            | |  |  _____|   | |
            | |  | |____     | |
            | |  '_.____''.  | |
            | |  | \____) |  | |
            | |   \______.'  | |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |    ______    | |
            | |  .' ____ \   | |
            | |  | |____\_|  | |
            | |  | '____`'.  | |
            | |  | (____) |  | |
            | |  '.______.'  | |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |   _______    | |
            | |  |  ___  |   | |
            | |  |_/  / /    | |
            | |      / /     | |
            | |     / /      | |
            | |    /_/       | |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |     ____     | |
            | |   .' __ '.   | |
            | |   | (__) |   | |
            | |   .`____'.   | |
            | |  | (____) |  | |
            | |  `.______.'  | |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |    ______    | |
            | |  .' ____ '.  | |
            | |  | (____) |  | |
            | |  '_.____. |  | |
            | |  | \____| |  | |
            | |   \______,'  | |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .------------------------. 
            | .----------------------. |
            | |     __      ____     | |
            | |    /  |   .'    '.   | |
            | |    `| |  |  .--.  |  | |
            | |     | |  | |    | |  | |
            | |    _| |_ |  `--'  |  | |
            | |   |_____| '.____.'   | |
            | |                      | |
            | '----------------------' |
             '------------------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |     _____    | |
            | |    |_   _|   | |
            | |      | |     | |
            | |   _  | |     | |
            | |  | |_' |     | |
            | |  `.___.'     | |
            | |              | |
            | '--------------' |
             '----------------'
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |    ___       | |
            | |  .'   '.     | |
            | | /  .-.  \    | |
            | | | |   | |    | |
            | | \  `-'  \_   | |
            | |  `.___.\__|  | |
            | |              | |
            | '--------------' |
             '----------------' 
            ''',
            '''
             .----------------. 
            | .--------------. |
            | |  ___  ____   | |
            | | |_  ||_  _|  | |
            | |   | |_/ /    | |
            | |   |  __'.    | |
            | |  _| |  \ \_  | |
            | | |____||____| | |
            | |              | |
            | '--------------' |
             '----------------' 
            '''
        ]
        self.mostrar_carta(figuras_cartas[self.cartas[-1] - 1])

if __name__ == '__main__':
    juego = Blackjack()
    juego.jugar()