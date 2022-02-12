"""
Datos de entrada
Distancia recorrida en kilometros -->y--> int
Datos de salida
Pago que debe realizar el cliente -->pa  = int
"""
# Entradas
y=int(input( "Inserte la distancia recorrida por usten en kilometros : "))


# Caja Negra 
d=(y-1000)# representa los kilometros adicionales que se cobraran despues de los 1000 km 

Precio=''
if (y<= 300):
    precio= 50_000
elif(y>300 and y<1000):
    precio= (70_000+(30000*(y-300))) # se cobra 30000 demas por cada km superior a 300 km
elif(y>1000):
    precio= ((150_000+(9000*(d)))+(((y-d)-300)*30000)) # Se cobra 9000 por cada km adicional despues de los 1000 km /se cobra 30000 demas por cada km superior a 300 km

# Salidas 
print(f" El Pago que debe realizar el cliente es de ${precio}")