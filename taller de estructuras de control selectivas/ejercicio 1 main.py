# Entrads
inversion = float(input("Ingrese la cantidad de dinero en inversión: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en porcentaje): "))

# Caja negra
intereses = inversion * (tasa_interes / 100)
if intereses > 100000:
    total_cuenta = inversion + intereses
else:
    total_cuenta = inversion + intereses

# Salidas
print("El total de dinero en la cuenta es: ${:.2f}".format(total_cuenta))