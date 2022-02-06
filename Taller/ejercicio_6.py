"""
mujer--> m-->int
hombre--> h-->int
"""
#entradas
m=int(input("Colocar cantidad de hombres "))
h=int(input("Colocar cantidad de mujeres "))
#Caja negra
p=(m+h)
Mi=(m*100)/p
Pi=(h*100)/p
#Salida
print("El promedio de mujeres es: ", Mi,"%")
print("El promedio de hombres: ", Pi,"%")

