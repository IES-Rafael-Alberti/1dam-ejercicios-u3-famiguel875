def crear_lista_compra():
    lista_compra = {}
    
    while True:
        articulo = input("Ingrese el artículo (o 'fin' para terminar): ")
        if articulo.lower() == 'fin':
            break
        precio = float(input("Ingrese el precio del artículo: "))
        lista_compra[articulo] = precio

    print("\nLista de la compra:")
    total_coste = 0
    for articulo, precio in lista_compra.items():
        print(f"{articulo}\t{precio}")
        total_coste += precio

    print(f"Total\t{total_coste}")

# Uso de la función
crear_lista_compra()
