Algoritmo Dinero_Banco
	//entradas
    Escribir "Ingrese el número de billetes de 50:"
    Leer billetes50
    Escribir "Ingrese el número de billetes de 20:"
    Leer billetes20
    Escribir "Ingrese el número de billetes de 10:"
    Leer billetes10
    Escribir "Ingrese el número de billetes de 5:"
    Leer billetes5
    Escribir "Ingrese el número de monedas de 1:"
    Leer monedas1
	//caja negra 
    total <- (billetes50 * 50) + (billetes20 * 20) + (billetes10 * 10) + (billetes5 * 5) + monedas1
	//salidas
    Escribir "El total de dinero es: ", total
FinAlgoritmo