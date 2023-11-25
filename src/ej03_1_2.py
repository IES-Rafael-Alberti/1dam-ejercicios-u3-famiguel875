def mostrar_mensaje_estudio(asignaturas):
    
    if not isinstance(asignaturas, list):
        raise ValueError("La entrada debe ser una lista.")

    for asignatura in asignaturas:
        print(f"Yo estudio {asignatura}")

# Ejemplo de uso
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
mostrar_mensaje_estudio(asignaturas)