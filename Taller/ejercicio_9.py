"""
Datos de entrada
precio de la hora-->K-->int
Horas trabajadas-->hts-->int
"""
#entrada
K=int(input("Exprese el precio de la hora "))
hts=int(input("Coloque las horas trabajadas "))
#Caja Negr
p=K*hts
w=0.2*p
Sln=p-w
#Salida
print("El sueldo neto es: ", Sln)