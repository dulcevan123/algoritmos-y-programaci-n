.Algoritmo Conversion_Metros
	//entradas
    Definir metros, pulgadas, pies, resto Pulgadas Como Real
    Escribir "Ingrese la cantidad en metros:"
    Leer metros
	//caja negra
    pulgadas <- metros * 39.27
    pies <- Trunc(pulgadas / 12)
    restoPulgadas <- pulgadas % 12
	//Salidas
    Escribir "La conversión es: ", pies, " pies y ", restoPulgadas, " pulgadas"
FinAlgoritmo