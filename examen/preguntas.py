#ACTIVIDAD 1:
#1. ¿Cuál es el nombre de la clase?
#   Producto
#
#2. ¿Cuáles son sus propiedades? 
#   Nombre, precio, total
#
#3. ¿Cuáles son sus métodos? 
#   init, calcularTotal, mostrarTotal
#
#4. ¿Qué función cumple __init__? 
#   Inicializa los atributos como el nombre y el precio
#
#5. ¿Para qué se utiliza self? 
#   Permite acceder a los atributos y métodos al mismo tiempo
#
#6. ¿En qué instrucción se crea un objeto? 
#   producto1 = Producto("Cuaderno", 35)
#
#7. ¿Cuál es el nombre del objeto? 
#   Cuaderno
#
#8. ¿Cómo se llama a calcularTotal()? 
#   from clases.Producto import calcularTotal
#
#9. ¿Qué valores recibe el constructor cuando se crea el objeto? 
#   "Cuaderno", 35
#
#10. ¿Qué resultado mostrará el programa? 
#    El costo de un cuadero o cuadernos comprados
#
#
#
#
#ACTIVIDAD 2:
class Rectangulo(object): 
    def __init__(self, base, altura): 
        # COMPLETAR: guardar las propiedades 
        self.base = base
        self.altura = altura
        self.area = 0
  
    def calcularArea(self, area): 
        # COMPLETAR: regresar el área 
        self.area = self.base * self.altura
  
    def mostrarArea(self): 
        # COMPLETAR: mostrar el resultado 
        print(f"El área total es: {self.area:.2f}")
  
# COMPLETAR: crear un objeto con base 8 y altura 5
rectangulo1 = Rectangulo (8, 5)

# COMPLETAR: llamar al método para mostrar el área 
rectangulo1.calcularArea()
rectangulo1.mostrarArea()




#ACTIVIDAD 3:
#1. ¿Cuál es la clase padre? 
#   class Operacion(object):
#
#2. ¿Cuál es la clase hija? 
#   class Multiplicacion(Operacion): 
#
#3. ¿Cómo se indica la herencia? 
#   Se pone entre parentesis el nombre de la primera clase que hicimos que es la clase padre
#
#4. ¿Qué propiedades utiliza la clase hija? 
#   self.numero1 y self.numero2
#
#5. ¿Por qué puede utilizarlas sin definir su propio __init__? 
#   Porque lo hereda de la clase padre
#
#6. ¿Por qué los métodos calcular() tienen resultados distintos? 
#   porque son diferentes operaciones, en la clase padre se suman y en la clase hijo se multiplican
#
#7. ¿Qué valores se imprimen? 
#   los resultados de las operaciones 12 y 32
#
#8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
#   No se podría llamar al procedimiento que esta integrado ahí
# 