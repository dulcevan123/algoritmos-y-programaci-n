suma = 0
k = 1
while suma < 1000:
    termino = (k**2 + 1) / k  
    suma += termino  
    k += 1  
print("Cantidad de términos necesarios:", k - 1)