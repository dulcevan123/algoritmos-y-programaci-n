Algoritmo ejercicio_7
	Definir numero1, i Como Entero
		Definir es_primo Como Logico
		
		Escribir "Ingrese un número entero:"
		Leer numero1
		
		Si numero1 <= 1 Entonces
			Escribir "No es primo"
		Sino
			es_primo <- Verdadero
			Para i <- 2 Hasta numero1-1 Con Paso 1 Hacer
				Si numero1 MOD i = 0 Entonces
					es_primo <- Falso
				FinSi
			FinPara
			
			Si es_primo Entonces
				Escribir "Es primo"
			Sino
				Escribir "No es primo"
			FinSi
		FinSi
FinAlgoritmo
