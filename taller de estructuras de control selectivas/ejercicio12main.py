#entradas
def desglosar_cantidad(cantidad):
    denominaciones = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
    resultado = {}
#caja negra
    for denominacion in denominaciones:
        cantidad_billetes_monedas, cantidad = divmod(cantidad, denominacion)
        if cantidad_billetes_monedas > 0:
            resultado[denominacion] = cantidad_billetes_monedas
#salida
    print(f'{cantidad_billetes_monedas} x {denominacion} COP')