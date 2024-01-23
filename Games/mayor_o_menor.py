import random

class MayorOMenor():
    MAYOR = "1"
    MENOR = "2"

    def __init__(self):
        self.cartas_exitosas = 0
        self.numero_actual = self.generar_numero()
        self.numero_siguiente = self.generar_numero()
    
    def jugar(self):
        print("Procura saber si la siguiente carta es mayor o menor entre 0 y 9.")
        while True:
            self.validar_numero_siguiente()
            self.mostrar_carta_actual()
            direccion = self.pedir_direccion()
            if not self.verificar_direccion(direccion):
                break
            self.numero_actual = self.numero_siguiente
        self.mostrar_mensaje_final()

    def generar_numero(self):
        return random.randint(0, 9)
    
    def validar_numero_siguiente(self):
        while self.numero_actual == self.numero_siguiente:
            self.numero_siguiente = self.generar_numero()

    def pedir_direccion(self):
        while True:
            print("1-Mayor\n2-Menor\nOpción:")
            texto_ingresado = input()
            if texto_ingresado in (self.MENOR, self.MAYOR):
                return texto_ingresado
        
    def verificar_direccion(self, direccion):
        if (self.numero_actual > self.numero_siguiente and direccion == self.MENOR) or \
           (self.numero_actual < self.numero_siguiente and direccion == self.MAYOR):
            self.cartas_exitosas += 1
            return True
        return False
            
    def mostrar_mensaje_final(self):
        cartas_plural = "cartas exitosas" if self.cartas_exitosas != 1 else "carta exitosa"
        print(f"Has conseguido {self.cartas_exitosas} {cartas_plural}. El último número fue {self.numero_siguiente}.")

    def mostrar_carta(self, carta):
        print(carta)

    def mostrar_carta_actual(self):
        figura = [
            '''
            .----------------. 
            | .--------------. |
            | |     ____     | |
            | |   .'    '.   | |
            | |  |  .--.  |  | |
            | |  | |    | |  | |
            | |  |  `--'  |  | |
            | |   '.____.'   | |
            | |              | |
            | '--------------' |
            '----------------' 
            ''',
            '''
            .----------------. 
            | .--------------. |
            | |     __       | |
            | |    /  |      | |
            | |    `| |      | |
            | |     | |      | |
            | |    _| |_     | |
            | |   |_____|    | |
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
            '''
        ]
        self.mostrar_carta(figura[self.numero_actual])

if __name__ == '__main__':
    juego = MayorOMenor()
    juego.jugar()