def ordenar_numeros_loteria(numeros):
    
    if not isinstance(numeros, list):
        raise ValueError("La entrada debe ser una lista.")

    numeros_ordenados = sorted(numeros)
    print(numeros_ordenados)
    return numeros_ordenados

numeros_ganadores = [int(x) for x in input("Ingresa los números ganadores separados por comas: ").split(',')]
ordenar_numeros_loteria(numeros_ganadores)