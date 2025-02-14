Algoritmo Promedio_General
	//entradas
    Definir matExam, matTarea, fisExam, fisTarea, quimExam, quimTarea, promedioMat, promedioFis, promedioQuim, promedioGeneral Como Real
    Escribir "Ingrese la calificación del examen de Matemática:"
    Leer matExam
    Escribir "Ingrese la calificación de la tarea de Matemática:"
    Leer matTarea
    Escribir "Ingrese la calificación del examen de Física:"
    Leer fisExam
    Escribir "Ingrese la calificación de la tarea de Física:"
    Leer fisTarea
    Escribir "Ingrese la calificación del examen de Química:"
    Leer quimExam
    Escribir "Ingrese la calificación de la tarea de Química:"
    Leer quimTarea
	//caja negra
    promedioMat <- (matExam * 0.70) + (matTarea * 0.30)
    promedioFis <- (fisExam * 0.60) + (fisTarea * 0.40)
    promedioQuim <- (quimExam * 0.80) + (quimTarea * 0.20)
    promedioGeneral <- (promedioMat + promedioFis + promedioQuim) / 3
	//salidas
    Escribir "El promedio general es: ", promedioGeneral
FinAlgoritmo