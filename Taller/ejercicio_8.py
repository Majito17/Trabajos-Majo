"""
datos de entrada
lado1-->w-->int
lado2-->e-->int
lado3-->r-->int

"""
#entrada
w=int(input("Ponga el lado 1 "))
e=int(input("Ponga el lado 2 "))
r=int(input("Ponga el lado 3 "))
#Caja Negra
s=(w+e+r)/2
are=(s*(s-w)*(s-e)*(s-r))**(1/2)
#Salida
print("El area es: ", are)