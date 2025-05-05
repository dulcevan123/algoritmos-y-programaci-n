estudiantes = {}

for i in range(1, 11):
    nombre = input(f"Ingrese el nombre del estudiante {i}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes[str(i)] = {"nombre": nombre, "nota": nota}

aprobados = [est["nombre"] for est in estudiantes.values() if est["nota"] >= 5]
suspendidos = [est["nombre"] for est in estudiantes.values() if est["nota"] < 5]
promedio = sum(est["nota"] for est in estudiantes.values()) / len(estudiantes)

print(f"\nEstudiantes aprobados: {aprobados}")
print(f"Estudiantes suspendidos: {suspendidos}")
print(f"Nota promedio de la clase: {promedio:.2f}")