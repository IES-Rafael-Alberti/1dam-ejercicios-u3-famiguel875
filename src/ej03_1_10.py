def encontrar_menor_mayor(precios):
    
    if not isinstance(precios, list):
        raise ValueError("La entrada debe ser una lista.")

    if not precios:
        print("La lista de precios está vacía.")
        return

    menor_precio = min(precios)
    mayor_precio = max(precios)

    print(f"El menor precio es: {menor_precio}")
    print(f"El mayor precio es: {mayor_precio}")