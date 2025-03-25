dividendo = int(input("Ingresa el dividendo: "))
divisor = int(input("Ingresa el divisor: "))
if divisor == 0:
    print("La división por cero no está definida.")
else:
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    residuo = dividendo
    print(f"Cociente: {cociente}, Residuo: {residuo}")
