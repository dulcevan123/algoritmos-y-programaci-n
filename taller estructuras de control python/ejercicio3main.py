# Entradas
sueldoBase = float(input("Introduce el sueldo base del vendedor: "))
venta1 = float(input("Introduce el monto de la primera venta: "))
venta2 = float(input("Introduce el monto de la segunda venta: "))
venta3 = float(input("Introduce el monto de la tercera venta: "))

# Caja negra
comision = 0.10
totalComisiones = (venta1 + venta2 + venta3) * comision
totalPago = sueldoBase + totalComisiones

# Salidas
print("El total de comisiones por las ventas es:", totalComisiones)
print("El pago total que recibirá el vendedor es:", totalPago)


