Algoritmo Area_Triangulo
	//entradas
    Escribir "Ingrese las longitudes de los tres lados del tri�ngulo:"
    Leer a, b, c
	//caja negra
    s = (a + b + c) / 2
    area = raiz(s * (s - a) * (s - b) * (s - c))
	//salidas
    Escribir "El �rea del tri�ngulo es: ", area
FinAlgoritmo
