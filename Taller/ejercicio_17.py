"""
Datos de entrada
Presupuesto-->p-->float
Datos de Salida
Presupuesto ginecologia-->g-->float
Presupuesto traumatologiaa-->t-->float
Presupuesto pediatria-->e-->float
"""
#entrada
p=float(input("Digite el presupuesto Total: "))
#caja negra
g=p*0.4
t=p*0.3
e=p*0.3
#salida
print("El presupuesto dedicado a ginecologia: ",g)
print("El presupuesto dedicado a traumatologia: ",t)
print("El presupuesto dedicado a pediatria: ",e)