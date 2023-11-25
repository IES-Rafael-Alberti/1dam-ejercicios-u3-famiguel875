def gestionar_informacion_persona():
    informacion_persona = {}
    
    while True:
        clave = input("Ingrese el dato que desea añadir (o 'fin' para terminar): ")
        if clave.lower() == 'fin':
            break
        valor = input(f"Ingrese el valor para {clave}: ")
        informacion_persona[clave] = valor
        print("Contenido del diccionario:", informacion_persona)

# Uso de la función
gestionar_informacion_persona()
