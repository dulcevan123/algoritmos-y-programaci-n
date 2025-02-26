def determinar_deporte(temperatura):
    if temperatura > 85:
        return "Natación"
    elif 70 < temperatura <= 85:
        return "Tenis"
    elif 32 < temperatura <= 70:
        return "Golf"
    elif 10 < temperatura <= 32:
        return "Esquí"
    else:
        return "Marcha"

# Ejemplo de uso con una temperatura de 50 grados Fahrenheit
temperatura = 50
deporte = determinar_deporte(temperatura)
print(f"A la temperatura de {temperatura}°F, el deporte apropiado es: {deporte}")


