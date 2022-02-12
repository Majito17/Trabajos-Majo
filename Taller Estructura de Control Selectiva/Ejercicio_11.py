"""
Datos De entrada
Temperatura-->t-->Float
Datos de Salida
Deporte-->d-->str
"""
#entrada
t=float(input("Digite la temperatura: "))
#Caja Negra
deporte=""
if(t>85):
    Deporte= "Natacion: "
elif(t>70 and t<=85):
    Deporte= "Tenis: "
elif(t>32 and t<=70):
    Deporte= "Golf: "
elif(t>12 and t<=32):
    Deporte= "Esqui: "
elif(t<=100):
    Deporte ="Marcha"
else:
    Deporte=" No se encuentra en el rango"
#Salida
print("El deporte es: ", Deporte)