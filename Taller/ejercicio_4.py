"""
Datos de entrada
valor_normal-->van-->int
Datos de salida
valor_final-->vaf-->float
"""
#Entrada
van=int(input("digite el valor normal de la compra: "))
#Caja negra
vaf=((van-(van*0.15)))
#Salidas
print("El valor final de la compra es: ", vaf)