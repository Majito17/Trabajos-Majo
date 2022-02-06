"""
Datos de entrada
Precio total-->p-->float
Precio de cuota-->c-->float
Datos de Salida
Porcentaje extra-->e-->float
"""
#entrada
p=float(input("Digite el precio total: "))
c=float(input("Digite el precio de la cuota: "))
#cajanegra
e=(p/12)-c
#salidas
print("El pocentaje extra ganado es; ", e, "%")