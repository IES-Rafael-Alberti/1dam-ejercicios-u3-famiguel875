def asignaturas_a_repetir(asignaturas):

    if not isinstance(asignaturas, list):
        raise ValueError("La entrada debe ser una lista.")

    asignaturas_aprobadas = []
    for asignatura in asignaturas:
        nota = input(f"Ingresa la nota para {asignatura}: ")
        try:
            nota = float(nota)
        except ValueError:
            raise ValueError("La nota debe ser un número válido.")
        
        if nota < 70:
            asignaturas_aprobadas.append(asignatura)

    asignaturas_a_repetir = list(set(asignaturas) - set(asignaturas_aprobadas))
    print(f"Asignaturas a repetir: {', '.join(asignaturas_a_repetir)}")
    return asignaturas_a_repetir

asignaturas_curso = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
asignaturas_a_repetir(asignaturas_curso)