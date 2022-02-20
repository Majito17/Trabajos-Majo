"""
h>=1000
+=(((k**2)+1)/k)
k range 1, inf
"""
k=1
h=0
lista=[]
while h<1000:
    h=(k**2+1)/k
    lista.append(h)
    k=k+1
print(len(lista))

