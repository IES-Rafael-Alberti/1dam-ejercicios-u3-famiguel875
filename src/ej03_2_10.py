def gestionar_base_datos_clientes():
    base_datos_clientes = {}

    while True:
        print("\nMenú:")
        print("(1) Añadir cliente")
        print("(2) Eliminar cliente")
        print("(3) Mostrar cliente")
        print("(4) Listar todos los clientes")
        print("(5) Listar clientes preferentes")
        print("(6) Terminar")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            nif = input("Ingrese el NIF del cliente: ")
            datos_cliente = {}
            datos_cliente['nombre'] = input("Ingrese el nombre del cliente: ")
            datos_cliente['direccion'] = input("Ingrese la dirección del cliente: ")
            datos_cliente['telefono'] = input("Ingrese el teléfono del cliente: ")
            datos_cliente['correo'] = input("Ingrese el correo del cliente: ")
            datos_cliente['preferente'] = input("¿Es cliente preferente? (True/False): ").lower() == 'true'
            base_datos_clientes[nif] = datos_cliente
        elif opcion == '2':
            nif = input("Ingrese el NIF del cliente a eliminar: ")
            if nif in base_datos_clientes:
                del base_datos_clientes[nif]
                print(f"Cliente con NIF {nif} eliminado.")
            else:
                print("El cliente no existe.")
        elif opcion == '3':
            nif = input("Ingrese el NIF del cliente a mostrar: ")
            if nif in base_datos_clientes:
                print(f"Datos del cliente con NIF {nif}:")
                for clave, valor in base_datos_clientes[nif].items():
                    print(f"{clave}: {valor}")
            else:
                print("El cliente no existe.")
        elif opcion == '4':
            print("\nLista de todos los clientes:")
            for nif, datos_cliente in base_datos_clientes.items():
                print(f"{nif}: {datos_cliente['nombre']}")
        elif opcion == '5':
            print("\nLista de clientes preferentes:")
            for nif, datos_cliente in base_datos_clientes.items():
                if datos_cliente['preferente']:
                    print(f"{nif}: {datos_cliente['nombre']}")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Uso de la función
gestionar_base_datos_clientes()
