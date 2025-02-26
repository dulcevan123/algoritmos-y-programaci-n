# Entrada
ventas_departamento1 = float(input("Ingrese las ventas del departamento 1: "))
ventas_departamento2 = float(input("Ingrese las ventas del departamento 2: "))
ventas_departamento3 = float(input("Ingrese las ventas del departamento 3: "))
ventas_totales = ventas_departamento1 + ventas_departamento2 + ventas_departamento3

# caja nega
if ventas_departamento1 > (0.33 * ventas_totales):
    incentivo1 = ventas_departamento1 * 0.2
else:
    incentivo1 = 0
if ventas_departamento2 > (0.33 * ventas_totales):
    incentivo2 = ventas_departamento2 * 0.2
else:
    incentivo2 = 0
if ventas_departamento3 > (0.33 * ventas_totales):
    incentivo3 = ventas_departamento3 * 0.2
else:
    incentivo3 = 0

# Salida
print(f"Incentivo Departamento 1: ${incentivo1:,.2f} COP")
print(f"Incentivo Departamento 2: ${incentivo2:,.2f} COP")
print(f"Incentivo Departamento 3: ${incentivo3:,.2f} COP")


