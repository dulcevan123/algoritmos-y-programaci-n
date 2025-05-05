usuarios = {
    "iperurena": {"nombre": "Iñaki", "apellido": "Perurena", "password": "123123"},
    "fmuguruza": {"nombre": "Fermín", "apellido": "Muguruza", "password": "654321"},
    "aolaizola": {"nombre": "Aimar", "apellido": "Olaízola", "password": "123456"}
}

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
        print(f"Acceso concedido. Bienvenido {usuarios[usuario]['nombre']} {usuarios[usuario]['apellido']}!")
        break
    else:
        intentos += 1
        print("Usuario o contraseña incorrectos. Intento", intentos)

if intentos == max_intentos:
    print("Has agotado tus intentos. Acceso bloqueado.")