"""
Datos De Entrada
Ventas Totales-->T-->float
Departamento 1-->u-->float
Departamento 2-->d--<float
Departamento 3-->t-->float
Salario Mensual-->m-->float
Datos Salida
Sueldo 1-->su-->float
Sueldo 2-->sd-->float
Sueldo 3-->st-->float
"""
#Entradas
T=float(input("Coloque las ventas totales: "))
u=float(input("Ingresa ventas departamento uno: "))
d=float(input("Ingresa ventas departamento dos: "))
t=float(input("Ingresa ventas departamento tres: "))
m=float(input("Ingrese el dinero ganado mesnsual: "))
#Caja Negra
pp=T*0.33
sb=m*0.20
if(u>pp):
    su=m+sb
else:
    su=m
if(d>pp):
    sd=m+sb
else:
    sd=m
if(t>pp):
    st=m+sb
else:
    st=m
#Salidas
print("El apartamento uno ganara: ", su)
print("El apartamento dos ganara: ", sd)
print("El apartamento tres ganara: ", st)
