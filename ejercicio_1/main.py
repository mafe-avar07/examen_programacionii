class Estacionamiento(object):

    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):

        if self.horas >= 1 and self.horas <= 2:
            pago = self.horas * 15

        elif self.horas >= 3 and self.horas <= 5:
            pago = self.horas * 12

        else:
            pago = self.horas * 10

        return pago

    def mostrarRecibo(self):

        print("RECIBO DE ESTACIONAMIENTO")
        print("Horas:", self.horas)
        print("Total a pagar: $", format(self.calcularPago(), ".2f"))


horas = int(input("Horas estacionadas: "))

if horas > 0:

    estacionamiento = Estacionamiento(horas)

    estacionamiento.mostrarRecibo()

else:
    print("Error: debes ingresar un número mayor que cero.")

