Algoritmo Ecuaciones_Lineales
	//entradas
    Definir a1, b1, c1, a2, b2, c2, determinante, x, y Como Real
    Escribir "Ingrese el coeficiente a1 de la primera ecuaci�n:"
    Leer a1
    Escribir "Ingrese el coeficiente b1 de la primera ecuaci�n:"
    Leer b1
    Escribir "Ingrese el t�rmino independiente c1 de la primera ecuaci�n:"
    Leer c1
    Escribir "Ingrese el coeficiente a2 de la segunda ecuaci�n:"
    Leer a2
    Escribir "Ingrese el coeficiente b2 de la segunda ecuaci�n:"
    Leer b2
    Escribir "Ingrese el t�rmino independiente c2 de la segunda ecuaci�n:"
    Leer c2
	//caja negra 
    determinante <- a1 * b2 - a2 * b1
    Si determinante <> 0 Entonces
        x <- (c1 * b2 - c2 * b1) / determinante
        y <- (a1 * c2 - a2 * c1) / determinante
		//salidas
        Escribir "La soluci�n del sistema es: x = ", x, " y = ", y
    Sino
        Escribir "El sistema no tiene soluci�n �nica."
    FinSi
FinAlgoritmo
