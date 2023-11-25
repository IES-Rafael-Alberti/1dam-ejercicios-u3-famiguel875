def mostrar_notas(asignaturas):
    
    if not isinstance(asignaturas, list):
        raise ValueError("La entrada debe ser una lista.")

    notas = {}
    for asignatura in asignaturas:
        nota = input(f"Ingresa la nota para {asignatura}: ")
        try:
            nota = float(nota)
        except ValueError:
            raise ValueError("La nota debe ser un número válido.")
        
        notas[asignatura] = nota

    for asignatura, nota in notas.items():
        print(f"En {asignatura} has sacado {nota}")

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
mostrar_notas(asignaturas)