"""
Datos de Entrada
Monto Compa-->c-->float
Datos Salias
Cantidad Invertidos Fondos-->f-->float
Credito a pagar-->p-->float
Pago interest-->i-->float
Cantidad Prestada-->a-->float
"""
#Entradas
c=float(input("Ingrese el valor total de las piezas: "))
#Caja Negra
if(c>5000000):
    pd=(c*0.55)
    pb=(c*0.30)
    cf=(c*0.15)
    i=(c*0.20)
elif (c>5000000):
    pd=(c*0.70)
    cf=(c*.30)
    i=(cf*0.20)
    pb=0
#Salida
print("La cantidad que se invierte de los fondos de la empresa: pd")
print("La cantidadque se debe pagar del credito es: ", cf)
print("El monto de los intereses es: ", i)
print("La cantidad que prestara el banco sera: ", pb)
