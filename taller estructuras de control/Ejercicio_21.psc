Algoritmo Ejercicio21
	//entadas
    Definir precio_contado, cuota_mensual, total_cuotas, recargo, porcentaje_recargo Como Entero
    Escribir "Introduce el precio de compra al contado (P) en COP: "
    Leer precio_contado
    Escribir "Introduce el pago mensual por cuota (T) en COP: "
    Leer cuota_mensual
	//caja negra
    total_cuotas <- cuota_mensual * 12
    recargo <- total_cuotas - precio_contado
    porcentaje_recargo <- (recargo * 100) / precio_contado
    //salidas
    Escribir "El porcentaje que se cobra por el recargo en el pago del computador por cuota es: ", porcentaje_recargo, "%"
FinAlgoritmo