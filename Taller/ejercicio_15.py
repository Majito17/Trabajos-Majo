"""
Datos de entrada
Precio Total-->pt-->float
Precio con descuento-->pd-->float
Datos de Salida
Porcentaje de descuento-->pd-->float
"""
#entradas
pt=float(input("Digite el Precio Total: "))
pd=float(input("Digite el precio con descuento: "))
#caja Negra
vd=((pt-pd)*pt)/100
#salidas
print("El porcentaje de descuento equivale a: ", vd, "%")