"""
Datos de entrada
Chelines austriacos-->ch-->float
Dracmas Griegos-->dc-->float
Pesetas-->p-->float
Datos de Salida
Pasetas-->ps-->float
Francos Franceses-->f-->float
Dolares EEUU-->d-->float
Liras Italianas--i-->float
"""
#ENTRADAS
ch=float(input("Digite la cantidad de chelines austriacos que quiera convertir: "))
dc=float(input("Digite la cantidad de Dracmas Griegos que quiera convertir: "))
p=float(input("Digite la cantidad de Pesetas que quiera convertir: "))
#Caja Negra
ps=(ch*956_871)/100
f=(dc*886.07)/20_110
d=(p/122_499)
i=(p*100)/9_289
#Salidas
print("El precio en pesetas sera: ", ps)
print("El precio en Francos Franceses sera: ", f)
print("El precio en Dolares EEUU sera: ",   d)
print("El precio en Liras Italianas sera: ", i)
