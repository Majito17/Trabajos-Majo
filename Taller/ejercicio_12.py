"""
Datos de entrada
examen matematicas-->em-->int
tarea 1 matematicas-->t1m-->int
tarea 2 matematicas-->t2m-->int
tarea 3 matematicas-->t3m-->int
examen fisica-->ef-->int
tarea 1 fisica-->t1f-->int
tarea 2 fisica-->t2f-->int
examen quimica-->eq-->int
tarea 1 quimica-->t1q-->int
tarea 2 quimica-->t2q-->int
tarea 3 quimica-->t3q-->int
Datos Salidas
promedio general-->pg-->float
promedio matematicas-->pm-->float
promedio fisica-->pf-->float
promedio quimica-->pq-->float
"""
#entradas
em=int(input("Digite calificacion examen matematicas: "))
t1m=int(input("Digite calificacion tarea 1 de matematicas: "))
t2m=int(input("Digite calificacion tarea 2 de matematicas: "))
t3m=int(input("Digite calificacion tarea 3 de matematicas: "))
ef=int(input("Digite calificacion examen fisica: "))
t1f=int(input("Digite calificacion tarea 1 de fisica: "))
t2f=int(input("Digite calificacion tarea 2 de fisica: "))
eq=int(input("Digite calificacion examen quimica: "))
t1q=int(input("Digite calificacion tarea 1 de quimica: "))
t2q=int(input("Digite calificacion tarea 2 de quimica: "))
t3q=int(input("Digite calificacion tarea 3 de quimica: "))
#caja negra
ptm=((t1m+t2m+t3m)/3)*0.1
pem=em*0.9
pgm=ptm+pem
ptf=((t1f+t2f)/2)*0.2
pef=ef*0.8
pgf=ptf+pef
ptq=((t1q+t2q+t3q)/3)*0.15
peq=eq*0.85
pgq=ptq+peq
pg=(pgm+pgf+pgq)/3
#salidas
print("Nota final matematicas: ", pgm)
print("Nota final fisica: ", pgf)
print("Nota final quimica: ", pgq)
print("Nota final general: ", pg)