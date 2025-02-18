# Entradas
horasNormales = float(input("Ingrese el número de horas normales trabajadas: "))
horasExtras = float(input("Ingrese el número de horas extras trabajadas: "))
precioHora = float(input("Ingrese el precio por hora normal: "))
precioHoraExtra = float(input("Ingrese el precio por hora extra: "))
deducciones = float(input("Ingrese el monto de las deducciones: "))
asignaciones = float(input("Ingrese el monto de las asignaciones: "))

# Caja negra
salarioBruto = (horasNormales * precioHora) + (horasExtras * precioHoraExtra) + asignaciones
salarioNeto = salarioBruto - deducciones

# Salidas
print("El salario neto es:", salarioNeto)





