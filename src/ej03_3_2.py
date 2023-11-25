def comparar_alumnos():
    nombres_primaria = set()
    nombres_secundaria = set()

    # Ingresar nombres de primaria
    while True:
        nombre = input("Ingrese el nombre de un alumno de primaria (o 'x' para terminar): ")
        if nombre.lower() == 'x':
            break
        nombres_primaria.add(nombre)

    # Ingresar nombres de secundaria
    while True:
        nombre = input("Ingrese el nombre de un alumno de secundaria (o 'x' para terminar): ")
        if nombre.lower() == 'x':
            break
        nombres_secundaria.add(nombre)

    # Mostrar resultados
    print("\nNombres de todos los alumnos de primaria:", nombres_primaria)
    print("Nombres de todos los alumnos de secundaria:", nombres_secundaria)

    nombres_comunes = nombres_primaria.intersection(nombres_secundaria)
    print("Nombres que se repiten entre primaria y secundaria:", nombres_comunes)

    nombres_solo_primaria = nombres_primaria - nombres_secundaria
    print("Nombres de primaria que no se repiten en secundaria:", nombres_solo_primaria)

    todos_en_secundaria = nombres_primaria.issubset(nombres_secundaria)
    print("¿Todos los nombres de primaria están incluidos en secundaria?", todos_en_secundaria)

# Uso de la función
comparar_alumnos()
