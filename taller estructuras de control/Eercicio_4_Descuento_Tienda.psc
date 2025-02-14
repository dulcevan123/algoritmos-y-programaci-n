Algoritmo Descuento_Tienda
	//entradas
    Definir totalCompra, descuento, totalPagar Como Real;
    Escribir "Ingrese el total de la compra:";
    Leer totalCompra;
	//caja negra
    descuento <- totalCompra * 0.15;
    totalPagar <- totalCompra - descuento;
	//salidas
    Escribir "El total a pagar con descuento es: ", totalPagar;
FinAlgoritmo
