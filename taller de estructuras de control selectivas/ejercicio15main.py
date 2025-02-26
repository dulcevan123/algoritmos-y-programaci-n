#entradas
def determinar_anemia(hemoglobina, edad, sexo):
#caja negra
    if edad < 1/12:  # 0 a 1 mes
        if 13 <= hemoglobina <= 26:
            return "Negativo"
        else:
            return "Positivo"
    elif 1/12 <= edad < 6/12:  # 1 a 6 meses
        if 10 <= hemoglobina <= 18:
            return "Negativo"
        else:
            return "Positivo"
    elif 6/12 <= edad < 1:  # 6 a 12 meses
        if 11 <= hemoglobina <= 15:
            return "Negativo"
        else:
            return "Positivo"
    elif 1 <= edad < 5:  # 1 a 5 años
        if 11.5 <= hemoglobina <= 15:
            return "Negativo"
        else:
            return "Positivo"
    elif 5 <= edad < 10:  # 5 a 10 años
        if 12.6 <= hemoglobina <= 15.5:
            return "Negativo"
        else:
            return "Positivo"
    elif 10 <= edad < 15:  # 10 a 15 años
        if 13 <= hemoglobina <= 15.5:
            return "Negativo"
        else:
            return "Positivo"
    elif sexo == "F" and edad >= 15:  # Mujeres mayores de 15 años
        if 12 <= hemoglobina <= 16:
            return "Negativo"
        else:
            return "Positivo"
    elif sexo == "M" and edad >= 15:  # Hombres mayores de 15 años
        if 14 <= hemoglobina <= 18:
            return "Negativo"
        else:
            return "Positivo"
    else:
        return "Datos no válidos"
#salidas
        print(f"El resultado del diagnóstico de anemia es: {resultado}")