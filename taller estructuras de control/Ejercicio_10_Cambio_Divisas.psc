Algoritmo Cambio_Divisas
	//entradas
    Definir chelines, dracmas, pesetas, dolares, liras, francos Como Real
    Escribir "Ingrese la cantidad en chelines austriacos:"
    Leer chelines
    pesetas <- chelines * 9.56871
    Escribir "El equivalente en pesetas es: ", pesetas
    
    Escribir "Ingrese la cantidad en dracmas griegos:"
    Leer dracmas
    pesetasDracmas <- dracmas * 0.88607
    francos <- pesetasDracmas / 20.110
    Escribir "El equivalente en francos franceses es: ", francos
    Escribir "Ingrese la cantidad en pesetas:"
    Leer pesetas
	//Caja negra 
    dolares <- pesetas / 122.499
    liras <- pesetas / 9.289
	//Salidas
    Escribir "El equivalente en dólares es: ", dolares
    Escribir "El equivalente en liras italianas es: ", liras
FinAlgoritmo