def calcular_aumento(categoria, sueldo_bruto):
    # Diccionario con los porcentajes de aumento según la categoría
    aumentos = {
        1: 0.10,
        2: 0.15,
        3: 0.20,
        4: 0.40,
        5: 0.60
    }

    # Verificar si la categoría es válida
    if categoria in aumentos:
        porcentaje_aumento = aumentos[categoria]
        nuevo_sueldo = sueldo_bruto * (1 + porcentaje_aumento)
        return nuevo_sueldo
    else:
        return "Categoría no válida"

# Datos del ejemplo
categoria = 3
sueldo_bruto = 2500000

nuevo_sueldo = calcular_aumento(categoria, sueldo_bruto)
if nuevo_sueldo == "Categoría no válida":
    print(nuevo_sueldo)
else:
    print(f"La nueva categoría del trabajador es: {categoria}")
    print(f"El nuevo sueldo bruto del trabajador es: {nuevo_sueldo:.2f} COP")


nuevo_sueldo = calcular_aumento(categoria, sueldo_bruto)
if nuevo_sueldo == "Categoría no válida":
    print(nuevo_sueldo)
else:
    print(f"La nueva categoría del trabajador es: {categoria}")
    print(f"El nuevo sueldo bruto del trabajador es: {nuevo_sueldo:.2f} COP")

