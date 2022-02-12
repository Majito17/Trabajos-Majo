"""
Datos De Entrada
Dato Uno-->u-->int
Dato dos-->d-->int
Datos Tres-->t-->int
Dato Cuatro-->c-->int
Datos Salida
Algoritmo-->l-->float
"""
#Entrada
from unicodedata import ucd_3_2_0


u=int(input("Escribir el primer numero: "))
d=int(input("Escribir el segundo numero: "))
t=int(input("Escribir el tercer numero: "))
c=int(input("Escribir el cuarto numero: "))
#Caja Ngra
if(c==0):
    l=(u-t)**2
elif(c>0):
        l=((u-d)**3)/c
#Salida
print("El valor sera: ", l)