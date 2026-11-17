
class Operacion(object):

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        resultado = self.numero1 + self.numero2
        return resultado

    def mostrarResultado(self):
        print("Resultado:", self.calcular())


class Resta(Operacion):

    def calcular(self):
        resultado = self.numero1 - self.numero2
        return resultado


numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

suma = Operacion(numero1, numero2)
resta = Resta(numero1, numero2)

print("Operación: Suma")
suma.mostrarResultado()

print("Operación: Resta")
resta.mostrarResultado()
