Algoritmo Descuento_Producto
	//entradas
    Definir precioFinal, precioPVP, descuento As Real
    Escribir "Ingrese el precio final del producto:"
    Leer precioFinal
    Escribir "Ingrese el precio de venta al público (PVP):"
    Leer precioPVP
	//caja negra 
    descuento <- ((precioPVP - precioFinal) / precioPVP) * 100
	//salidas
    Escribir "El porcentaje de descuento es: ", descuento, "%"
FinAlgoritmo
