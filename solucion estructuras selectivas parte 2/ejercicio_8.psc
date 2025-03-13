Algoritmo ejercicio_8
	Definir Calificacion como real 
	Escribir "insertar calificacion del estudiante:"
	Leer calificacion
	Si calificacion >=90 Entonces
		Escribir "A"
	SiNo
		Si calificacion >= 80 Y calificacion <90 Entonces
			Escribir "B"
		SiNo
			Si calificacion >=70 Y calificacion <80 Entonces
				Escribir "C"
			SiNo
				Si calificacion >=60 Y calificacion <70 Entonces
					Escribir "D"
				SiNo
					Si calificacion <60 Entonces
						Escribir "F"
					SiNo
						
					Fin Si
				Fin Si
			Fin Si
			
		Fin Si
	Fin Si
FinAlgoritmo
