def formatear_fecha():
    fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
    partes_fecha = fecha.split('/')
    mes_nombre = "mes_desconocido"
    meses = ['', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    if len(partes_fecha) == 3 and partes_fecha[1].isdigit() and partes_fecha[2].isdigit():
        mes_numero = int(partes_fecha[1])
        if 1 <= mes_numero <= 12:
            mes_nombre = meses[mes_numero]
    print(f"{partes_fecha[0]} de {mes_nombre} de {partes_fecha[2]}")

# Uso de la función
formatear_fecha()
