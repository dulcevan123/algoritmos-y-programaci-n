#entrada
def calcular_monto_energia(lectura_anterior, lectura_actual):
    consumo = lectura_actual - lectura_anterior
#caja negra
    if consumo <= 100:
        costo = consumo * 600
    elif consumo <= 300:
        costo = 100 * 600 + (consumo - 100) * 900
    elif consumo <= 500:
        costo = 100 * 600 + 200 * 900 + (consumo - 300) * 1000
    else:
        costo = 100 * 600 + 200 * 900 + 200 * 1000 + (consumo - 500) * 1200
    return costo
#salida
    print(es_primo(numero))  

