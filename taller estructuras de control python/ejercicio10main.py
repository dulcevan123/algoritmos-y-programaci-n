# Entradas
chelines = float(input("Ingrese la cantidad en chelines austriacos: "))
pesetas = chelines * 9.56871
print("El equivalente en pesetas es:", pesetas)

dracmas = float(input("Ingrese la cantidad en dracmas griegos: "))
pesetasDracmas = dracmas * 0.88607
francos = pesetasDracmas / 20.110
print("El equivalente en francos franceses es:", francos)

pesetas = float(input("Ingrese la cantidad en pesetas: "))

# Caja negra
dolares = pesetas / 122.499
liras = pesetas / 9.289

# Salidas
print("El equivalente en dólares es:", dolares)
print("El equivalente en liras italianas es:", liras)




