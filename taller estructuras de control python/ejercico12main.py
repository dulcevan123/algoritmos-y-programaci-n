# Entradas
matExam = float(input("Ingrese la calificación del examen de Matemática: "))
matTarea = float(input("Ingrese la calificación de la tarea de Matemática: "))
fisExam = float(input("Ingrese la calificación del examen de Física: "))
fisTarea = float(input("Ingrese la calificación de la tarea de Física: "))
quimExam = float(input("Ingrese la calificación del examen de Química: "))
quimTarea = float(input("Ingrese la calificación de la tarea de Química: "))

# Caja negra
promedioMat = (matExam * 0.70) + (matTarea * 0.30)
promedioFis = (fisExam * 0.60) + (fisTarea * 0.40)
promedioQuim = (quimExam * 0.80) + (quimTarea * 0.20)
promedioGeneral = (promedioMat + promedioFis + promedioQuim) / 3

# Salidas
print("El promedio general es:", promedioGeneral)






