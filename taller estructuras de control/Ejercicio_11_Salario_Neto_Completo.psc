Algoritmo Salario_Neto_Completo
	//entradas
    Definir horasNormales, horasExtras, precioHora, precioHoraExtra, deducciones, asignaciones, salarioBruto, salarioNeto Como Real
    Escribir "Ingrese el número de horas normales trabajadas:"
    Leer horasNormales
    Escribir "Ingrese el número de horas extras trabajadas:"
    Leer horasExtras
    Escribir "Ingrese el precio por hora normal:"
    Leer precioHora
    Escribir "Ingrese el precio por hora extra:"
    Leer precioHoraExtra
    Escribir "Ingrese el monto de las deducciones:"
    Leer deducciones
    Escribir "Ingrese el monto de las asignaciones:"
    Leer asignaciones
	//caja negra 
    salarioBruto <- (horasNormales * precioHora) + (horasExtras * precioHoraExtra) + asignaciones
    salarioNeto <- salarioBruto - deducciones
	//salidas
    Escribir "El salario neto es: ", salarioNeto
FinAlgoritmo