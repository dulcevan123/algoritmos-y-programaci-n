def calcular_descuento(monto):
    if monto < 50000:
        descuento = 0
    elif 50000 <= monto <= 100000:
        descuento = 0.05
    elif 100000 < monto <= 700000:
        descuento = 0.11
    elif 700000 < monto <= 1500000:
        descuento = 0.18
    else:
        descuento = 0.25
    
    monto_descuento = monto * descuento
    monto_a_pagar = monto - monto_descuento
    return monto_descuento, monto_a_pagar

nombre_cliente = "Juan"
monto_compra = 120000

print(f"Nombre del cliente: {nombre_cliente}")
print(f"Monto de la compra: {monto_compra:.2f} COP")



