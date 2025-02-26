# Entrada
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))
D = int(input("Ingrese el valor de D: "))

# Proceso
# Formar el número N
N = int(f"{A}{B}{C}{D}")

# Redondear a la centena más próxima
if N % 100 >= 50:
    centena_mas_proxima = (N // 100 + 1) * 100
else:
    centena_mas_proxima = (N // 100) * 100

# Salida
print(f"El número {N} redondeado a la centena más próxima es: {centena_mas_proxima}")


