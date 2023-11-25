def mostrar_informacion_persona():
    datos_persona = {}
    datos_persona['nombre'] = input("Ingrese su nombre: ")
    datos_persona['edad'] = input("Ingrese su edad: ")
    datos_persona['direccion'] = input("Ingrese su dirección: ")
    datos_persona['telefono'] = input("Ingrese su número de teléfono: ")

    print(f"{datos_persona['nombre']} tiene {datos_persona['edad']} años, vive en {datos_persona['direccion']} y su número de teléfono es {datos_persona['telefono']}")

# Uso de la función
mostrar_informacion_persona()
