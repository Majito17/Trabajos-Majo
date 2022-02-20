lista=[]
numero=int(input("numero 1 para agregar una altura y numero 2 para buscar el numero mas grande"))
n=0
while True:
    if(numero==1):
        j=float(input("altura"))
        numero=int(input("numero 1 para agregar una altura y numero 2 para buscar el numero mas grande"))
        lista.append(j)
    elif(numero==2):
        print("la mayor altura:", max(lista)) 
        break