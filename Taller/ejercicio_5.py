"""
Datos de entrada
nota_1-->n1-->int
nota_2-->n2-->int
nota_3-->n3-->int
examen_final-->exfi-->int
trabajo_final-->tf-->int
Datos de salida
calificacion_final-->cf-->float
"""
#Entradas
n1=int(input("Escriba Nota uno: "))
n2=int(input("Escriba Nota dos: "))
n3=int(input("Escriba Nota tres: "))
exfi=int(input("Digite la nota del examen final: "))
tf=int(input("Digite la nota del trabajo final: "))
#Caja negra
cp=((n1+n2+n3)/3)*0.55
ef=(exfi*0.30)
tfs=(tf*0.15)
cafi=(cp+ef+tfs)
#Salida
print("La calificacion final de computacion es: ", cafi)