Algoritmo ejercicio_6
		Definir a�o Como Entero
		
		Escribir "Ingrese el a�o:"
		Leer a�o
		
		Si (a�o MOD 4 == 0) Entonces
			Si (a�o MOD 100 <> 0) Entonces
				Escribir "Es bisiesto"
			Sino
				Si (a�o MOD 400 == 0) Entonces
					Escribir "Es bisiesto"
				Sino
					Escribir "No es bisiesto"
				FinSi
			FinSi
		Sino
			Escribir "No es bisiesto"
		FinSi
FinAlgoritmo
