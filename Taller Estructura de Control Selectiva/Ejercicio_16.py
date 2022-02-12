"""
Datos de entrada
valor de w --> w --> int
valor de v --> v --> int
valor de q --> q --> int
Datos de salida
valor de x--> x --> str
valor de x2--> x2 -->str
"""
#entradas
from cmath import sqrt
w=int(input("valor de a"))
v=int(input("valor de b"))
q=int(input("valor de c"))
d= v**2-4*w*q
#caja negra
if(d==0):
    x=x2=-v/(2*w)
    print("el valor de x1 es:", str(x), "y el valor de x2 es:", str(x2))
elif(d>0):
    x=(-v+sqrt(v**2-4*w*q))/(2*w)
    x2=(-v-sqrt(v**2-4*w*q))/(2*w)
    print("el valor de x1 es:", str(x), "y el valor de x2 es:", str(x2))
else:
    print("no tiene solucion en los reales")
#salida