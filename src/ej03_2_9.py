def gestionar_facturas():
    facturas = {}

    while True:
        opcion = input("¿Qué desea hacer? (1: Añadir factura, 2: Pagar factura, 3: Terminar): ")

        if opcion == '1':
            numero_factura = input("Ingrese el número de factura: ")
            coste_factura = float(input("Ingrese el coste de la factura: "))
            facturas[numero_factura] = coste_factura
        elif opcion == '2':
            numero_factura = input("Ingrese el número de factura a pagar: ")
            if numero_factura in facturas:
                coste_pagado = facturas.pop(numero_factura)
                print(f"Factura {numero_factura} pagada. Cantidad pagada hasta el momento: {sum(facturas.values())}, Cantidad pendiente de cobro: {coste_pagado}")
            else:
                print("La factura no existe.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Uso de la función
gestionar_facturas()
