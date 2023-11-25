def filtrar_abecedario():
    """
    Almacena el abecedario en una lista, elimina las letras que ocupan posiciones múltiplos de 3
    y muestra por pantalla la lista resultante.

    Example:
    >>> filtrar_abecedario()
    ['A', 'B', 'D', 'E', 'G', 'H', 'K', 'M', 'N', 'P', 'Q', 'T', 'V', 'X', 'Z']
    """
    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    abecedario_filtrado = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]
    print(abecedario_filtrado)
    return abecedario_filtrado

filtrar_abecedario()