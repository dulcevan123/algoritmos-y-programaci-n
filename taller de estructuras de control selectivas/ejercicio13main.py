#entradas
def obtener_zodiaco(fecha_nacimiento):
    signos = [
        ("Sagitario", (11, 22), (12, 21)),
        ("Capricornio", (12, 22), (1, 20)),
        ("Acuario", (1, 21), (2, 19)),
        ("Piscis", (2, 20), (3, 20)),
        ("Aries", (3, 21), (4, 20)),
        ("Tauro", (4, 21), (5, 21)),
        ("Géminis", (5, 22), (6, 21)),
        ("Cáncer", (6, 22), (7, 21)),
        ("Leo", (7, 22), (8, 23)),
        ("Virgo", (8, 24), (9, 23)),
        ("Libra", (9, 24), (10, 23)),
        ("Escorpio", (10, 24), (11, 21))
    ]
  #caja negra  
    dia, mes, anio = map(int, fecha_nacimiento.split("/"))
    fecha_nacimiento_dt = datetime(anio, mes, dia)
    
    for signo, (mes_inicio, dia_inicio), (mes_fin, dia_fin) in signos:
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
            edad = datetime.now().year - anio
            return signo, edad
    #salidas
    return "Signo no encontrado", 0
    print(f"Signo del zodiaco: {signo}, Edad: {edad} años")
