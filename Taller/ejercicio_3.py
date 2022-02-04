""""
Datos de entrada
sueldo_base-->su_ba-->int
ventas_total-->ve_to-->int
Datos de salida
comision-->com-->float
ganancia_total-->gat-->float
"""
#Entrada
su_ba=int(input("digite el sueldo base"))
ve_to=int(input("digite el dinero total de las ventas: "))
#Caja negra
com=(ve_to*0.10)
gat=(su_ba+com)
#Salidas
print(f"Obtendra de comisiones: {com}")
print(f"Su sueldo total sera de: {gat}")