"""
Datos de entrada
Numero de Galones-->n-->float
Datos de Salida
Precio de la gasolina-->p-->float
"""
#entradas
n=float(input("Digite el numero de galones: "))
#Caja negra
l=n*3.785
p=l*50000
#salidas
print("El precio de la gasolina es: ", p)