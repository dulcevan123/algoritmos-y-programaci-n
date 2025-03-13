Algoritmo ejercicio_6
		Definir año Como Entero
		
		Escribir "Ingrese el año:"
		Leer año
		
		Si (año MOD 4 == 0) Entonces
			Si (año MOD 100 <> 0) Entonces
				Escribir "Es bisiesto"
			Sino
				Si (año MOD 400 == 0) Entonces
					Escribir "Es bisiesto"
				Sino
					Escribir "No es bisiesto"
				FinSi
			FinSi
		Sino
			Escribir "No es bisiesto"
		FinSi
FinAlgoritmo
