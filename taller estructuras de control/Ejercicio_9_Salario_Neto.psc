Algoritmo Salario_Neto
	//entradas
    Definir horasTrabajadas, precioHora, salarioBruto, salarioNeto Como Real
    Escribir "Ingrese el número de horas trabajadas:"
    Leer horasTrabajadas
    Escribir "Ingrese el precio por hora:"
    Leer precioHora
	//caja negra 
    salarioBruto <- horasTrabajadas * precioHora
    salarioNeto <- salarioBruto * 0.80
	//salidas
    Escribir "El salario neto es: ", salarioNeto
FinAlgoritmo