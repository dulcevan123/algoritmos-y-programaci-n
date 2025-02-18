# Entradas
horasTrabajadas = float(input("Ingrese el número de horas trabajadas: "))
precioHora = float(input("Ingrese el precio por hora: "))

# Caja negra
salarioBruto = horasTrabajadas * precioHora
salarioNeto = salarioBruto * 0.80

# Salidas
print("El salario neto es:", salarioNeto)




