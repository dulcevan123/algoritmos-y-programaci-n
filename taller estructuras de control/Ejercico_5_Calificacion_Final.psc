Algoritmo Calificacion_Final
	//entradas
    Definir parcial1, parcial2, parcial3, examenFinal, trabajoFinal,promedioParciales, calificacionFinal Como Real;
    Escribir "Ingrese la calificación del primer parcial:";
    Leer parcial1;
    Escribir "Ingrese la calificación del segundo parcial:";
    Leer parcial2;
    Escribir "Ingrese la calificación del tercer parcial:";
    Leer parcial3;
    Escribir "Ingrese la calificación del examen final:";
    Leer examenFinal;
    Escribir "Ingrese la calificación del trabajo final:";
    Leer trabajoFinal;
	//caja negra
    promedioParciales <- (parcial1 + parcial2 + parcial3) / 3;calificacionFinal <- (promedioParciales * 0.55 )+(examenFinal * 0.30)+(trabajoFinal * 0.15);
	//salidas
    Escribir "La calificación final es: ", calificacionFinal;
FinAlgoritmo