"""
Datos de entrada
Lectura Actual-->l-->float
Lectura Anterior-->a-->float
precio por kilovatio--k-->float
Datos de Salida
Precio del recibo-->r-->float
"""
#entradas
l=float(input("Digite cual es la lectura actual: "))
a=float(input("Digite cual es la lectura anterior: "))
k=float(input("Digite el precio por kilovatio: "))
#cajanegra
r=(l-a)*k
#salidas
print("El costo del recibo sera de: ", r)