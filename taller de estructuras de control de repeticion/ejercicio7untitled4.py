max_altura = 0
cantidad_estudiantes = int(input("Ingresa la cantidad de estudiantes: "))
for i in range(cantidad_estudiantes):
    altura = float(input(f"Ingrese la altura del estudiante {i + 1} (en cm): "))
    if altura > max_altura:
        max_altura = altura
print(f"La altura máxima entre los estudiantes es: {max_altura} cm")