Algoritmo ejercicio_9
    Escribir "Ingrese un n�mero:"
    Leer numero
    numero_str = convertirATexto (numero)
    reverso_str = ""
	
    Para i = longitud(numero_str) Hasta 1 Con Paso -1 Hacer
        reverso_str = concatenar(reverso_str, subcadena(numero_str, i, i))
    FinPara
	
    Si numero_str = reverso_str Entonces
        Escribir "Es un pal�ndromo"
    Sino
        Escribir "No es un pal�ndromo"
    FinSi
FinAlgoritmo

