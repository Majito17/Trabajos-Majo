#Entrada
la=int(input("Ingrese la lectura actual: "))
le=int(input("Ingrese la lectura anterior: "))
#Caja negra
lnc=le-la
if(lnc>=0) and (lnc<=100):
    s=lnc*4600
elif(lnc>=101) and (lnc<=300):
    s=lnc*80000
elif(lnc>=301) and (lnc<=500):
    s=lnc*100000
elif(lnc>=501):
    s=lnc*120000
#Salida
print("El monto a pagar sera: ", s)