# Entradas
parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
examenFinal = float(input("Ingrese la calificación del examen final: "))
trabajoFinal = float(input("Ingrese la calificación del trabajo final: "))

# Caja negra
promedioParciales = (parcial1 + parcial2 + parcial3) / 3
calificacionFinal = (promedioParciales * 0.55) + (examenFinal * 0.30) + (trabajoFinal * 0.15)

# Salidas
print("La calificación final es:", calificacionFinal)



