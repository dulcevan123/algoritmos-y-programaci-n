Algoritmo Ecuaciones_Lineales
	//entradas
    Definir a1, b1, c1, a2, b2, c2, determinante, x, y Como Real
    Escribir "Ingrese el coeficiente a1 de la primera ecuación:"
    Leer a1
    Escribir "Ingrese el coeficiente b1 de la primera ecuación:"
    Leer b1
    Escribir "Ingrese el término independiente c1 de la primera ecuación:"
    Leer c1
    Escribir "Ingrese el coeficiente a2 de la segunda ecuación:"
    Leer a2
    Escribir "Ingrese el coeficiente b2 de la segunda ecuación:"
    Leer b2
    Escribir "Ingrese el término independiente c2 de la segunda ecuación:"
    Leer c2
	//caja negra 
    determinante <- a1 * b2 - a2 * b1
    Si determinante <> 0 Entonces
        x <- (c1 * b2 - c2 * b1) / determinante
        y <- (a1 * c2 - a2 * c1) / determinante
		//salidas
        Escribir "La solución del sistema es: x = ", x, " y = ", y
    Sino
        Escribir "El sistema no tiene solución única."
    FinSi
FinAlgoritmo
