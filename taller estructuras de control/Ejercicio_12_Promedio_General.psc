Algoritmo Promedio_General
	//entradas
    Definir matExam, matTarea, fisExam, fisTarea, quimExam, quimTarea, promedioMat, promedioFis, promedioQuim, promedioGeneral Como Real
    Escribir "Ingrese la calificaci�n del examen de Matem�tica:"
    Leer matExam
    Escribir "Ingrese la calificaci�n de la tarea de Matem�tica:"
    Leer matTarea
    Escribir "Ingrese la calificaci�n del examen de F�sica:"
    Leer fisExam
    Escribir "Ingrese la calificaci�n de la tarea de F�sica:"
    Leer fisTarea
    Escribir "Ingrese la calificaci�n del examen de Qu�mica:"
    Leer quimExam
    Escribir "Ingrese la calificaci�n de la tarea de Qu�mica:"
    Leer quimTarea
	//caja negra
    promedioMat <- (matExam * 0.70) + (matTarea * 0.30)
    promedioFis <- (fisExam * 0.60) + (fisTarea * 0.40)
    promedioQuim <- (quimExam * 0.80) + (quimTarea * 0.20)
    promedioGeneral <- (promedioMat + promedioFis + promedioQuim) / 3
	//salidas
    Escribir "El promedio general es: ", promedioGeneral
FinAlgoritmo