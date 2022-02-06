"""
Datos de entrada
Prestamo inicial-->s-->float
Datos de Salida
Porcentaje anual-->pa-->float
"""
#entradas
s=float(input("Ingrese el capital del prestamo: "))
#Caja Negra
pa=(s*4)/100
#salida
print("El porcentaje anual equivale: ", pa, "%")
