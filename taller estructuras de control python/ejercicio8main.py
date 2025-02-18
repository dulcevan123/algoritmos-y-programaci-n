import math

# Entradas
a = float(input("Ingrese la longitud del primer lado del triángulo: "))
b = float(input("Ingrese la longitud del segundo lado del triángulo: "))
c = float(input("Ingrese la longitud del tercer lado del triángulo: "))

# Caja negra
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Salidas
print("El área del triángulo es:", area)




