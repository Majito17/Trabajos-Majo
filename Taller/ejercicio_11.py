"""
Datos de entrada
Numero de Horas-->h-->int
Numero de Horas Extra-->e-->int
Sueldo por Hora-->s-->float
Numero de Hijos-->hj-->int
Datos de Salida
Asignaciones-->a-->float
Deducciones-->d-->float
Sueldo Neto-->n-->float
"""
#entradas
h=int(input("Digite el numero de horas: "))
e=int(input("Digite el numero de horas extras: "))
s=float(input("Digite el sueldo por hora: "))
hj=int(input("Digite el numero de hijos: "))
#caja negra
sb=h*s
he=(s*0.25)+s
se=he*e
a=se+430_000+(173_000*hj)
d=sb*0.14
n=sb+a-d
#salida
print("Sus Asignaciones fueron: ", a)
print("Sus Deducciones fueron: ", d)
print("Su Sueldo Neto fue: ", n)
