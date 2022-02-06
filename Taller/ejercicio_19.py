"""
Datos de entrada
Numero de naranjas-->n-->int
Ventas Finales-->v-->float
Datos de Salida
Porcentaje de ganacias-->g-->float
"""
#entradas
n=int(input("Digite la cantidad de naranjas: "))
v=float(input("Digitar las ventas Finales: "))
#Caja nEGRA
c=(n/12)*6
g=(v-c)
pg=(g*100)/c
#salidas
print("El porcentaje que se ganara es de: ",pg, "%")
