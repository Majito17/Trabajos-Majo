"""
Datos de entrada
Numero de billetes de 50000-->nb5000-->int
Numero de billetes de 20000-->nb200-->int
Numero de billetes de 10000-->nb100-->int
Numero de billetes de 5000-->nb50-->int
Numero de billetes de 2000-->nb20-->int
Numero de billetes de 1000-->nb10-->int
Numero de billetes de 500-->nb5-->int
Numero de billetes de 100-->nb1-->int
Datos de Salida
Dinero Total-->D-->int
"""
#entradas
nb500=int(input("Digite el numero de billetes de 50000: "))
nb200=int(input("Digite el numero de billetes de 20000: "))
nb100=int(input("Digite el numero de billetes de 10000: "))
nb50=int(input("Digite el numero de billetes de 5000: "))
nb20=int(input("Digite el numero de billetes de 2000: "))
nb10=int(input("Digite el numero de billetes de 1000: "))
nb5=int(input("Digite el numero de billetes de 500: "))
nb1=int(input("Digite el numero de billetes de 100: "))
#Caja Negra
D=(nb500*50000)+(nb200*20000)+(nb100*10000)+(nb50*5000)+(nb20*2000)+(nb10*1000)+(nb5*500)+(nb1*100)
#salida
print("El dinero total sera: ", D)