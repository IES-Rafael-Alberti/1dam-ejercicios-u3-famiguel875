def mostrar_numeros_inverso():

    numeros = list(range(1, 11))
    numeros_inverso = list(reversed(numeros))
    print(', '.join(map(str, numeros_inverso)))
    return numeros_inverso

mostrar_numeros_inverso()