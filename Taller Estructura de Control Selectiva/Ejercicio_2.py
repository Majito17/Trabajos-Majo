"""
Datos De entrada
El sueldo del trabajador-->t-->float
Datos De Salida
Nuevo Sueldo-->m-->float
"""
#Entrada
t=float(input("Ingrese el sueldo del trabajor por favor: "))
#Caja Negra
if(t<900_000):
    n=t*0.15
    m=t+n
else:
    n=t*0.12
    m=t+n
#Salida
print("El nuevo salario seria: ", m)