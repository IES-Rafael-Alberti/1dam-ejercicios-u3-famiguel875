def mostrar_asignaturas(asignaturas):

    if not isinstance(asignaturas, list):
        raise ValueError("La entrada debe ser una lista.")

    for asignatura in asignaturas:
        print(asignatura)

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
mostrar_asignaturas(asignaturas)