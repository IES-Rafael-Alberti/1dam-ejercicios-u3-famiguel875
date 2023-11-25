def conjuntos_letras():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    consonantes = alfabeto - vocales
    letras_comunes = vocales.intersection(consonantes)

    print("Conjunto de consonantes:", consonantes)
    print("Letras comunes entre vocales y consonantes:", letras_comunes)

# Uso de la función
conjuntos_letras()
