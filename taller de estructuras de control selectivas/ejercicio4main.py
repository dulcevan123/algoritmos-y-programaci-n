# Entrada
monto_total = float(input("Ingrese el monto total de la compra: "))

# caja negra
if monto_total > 5000000:
    inversion = monto_total * 0.55
    credito = monto_total * 0.30
    intereses = monto_total * 0.15
    monto_total = inversion + credito + intereses
else:
    inversion = monto_total
    credito = 0
    intereses = 0

# Salida
print(f"Inversión: ${inversion:,.2f} COP")
print(f"Pago a crédito: ${credito:,.2f} COP")
print(f"Intereses: ${intereses:,.2f} COP")
print(f"Monto total: ${monto_total:,.2f} COP")

