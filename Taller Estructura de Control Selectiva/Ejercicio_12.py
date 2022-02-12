"""
entradas--> Valor float en una cantidad de pesos Colombianos COP
COP-->float-->u
Salidas--> u descompuesto en billetes y monedas
u esta decompuesto por -->str --> Lista0
"""
#Entrada
u=float(input("\nDime una cantidad en COP: "))
#Caja Ngra
lista=[]
for j in [100000,50000,20000,10000,5000,2000,1000,500,200,100,50]:
    if u >= j:
        lista.append(int(u/j)*j)
        u=u - int(u/j)*j
    else:
        u=u
    Lista2=str(lista)[1: -1]
#Salida
print(Lista2,"\n")
