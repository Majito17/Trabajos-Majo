"""
Datos de entrada
Cantidad Invertida-->I-->float
Intereses-->int-->float
Datos de Salidas
Dinero Final-->f-->float
"""
#Entradas
I=float(input("Ingrese la cantidad de dinero invertido: "))
int=float(input("ingrese el porcentaje de interes: "))
#Caja Negra
dinero=""
nt=(I*int)/100
if(I>100000):
    dinero=print("se reinvertir: ",(I+nt))
else:     
    dinero=print("no se reinvierte ",I)
#Salida
print(dinero)
