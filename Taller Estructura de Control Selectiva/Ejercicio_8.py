"""
Datos de entrada
Primer valor entero -->u-->int
Segundo valor entero -->j-->int
Datos de salida
Caso afirmativo = " Los valores de u y j satisfacen la expresion "
Caso Negativo = " Los valores de u y j no satisfacen la expresion "
"""
# Entradas
u=int(input( "Inserte el valor que le dara a U : "))
j=int(input( "Inserte el valor que le dara a J : "))
# Caja Negra 
resultado=''
if ((u**3 + j**4 - 2*u**2) > 680):
    resultado=(f"Los valores de U: {u} y J :{j} satisfacen la expresion ")
else:
    resultado=(f"Los valores de U :{u} y J :{j} no satisfacen la expresion ")

# Salidas 
print(f"{resultado}")