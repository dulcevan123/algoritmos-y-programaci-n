Algoritmo Presupuesto_Hospital
	//entradas
    Definir presupuestoTotal, presupuestoUrgencias, presupuestoPediatria, presupuestoTraumatologia Como Real
    Escribir "Ingrese el presupuesto total anual:"
    Leer presupuestoTotal
	//caja negra
    presupuestoUrgencias <- presupuestoTotal * 0.37
    presupuestoPediatria <- presupuestoTotal * 0.42
    presupuestoTraumatologia <- presupuestoTotal * 0.21
	//salidas
    Escribir "El presupuesto para Urgencias es: ", presupuestoUrgencias
    Escribir "El presupuesto para Pediatr�a es: ", presupuestoPediatria
    Escribir "El presupuesto para Traumatolog�a es: ", presupuestoTraumatologia
FinAlgoritmo