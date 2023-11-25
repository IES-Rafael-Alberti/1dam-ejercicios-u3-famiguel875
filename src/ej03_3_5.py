def encontrar_interseccion():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pares = {num for num in numeros if num % 2 == 0}
    multiplos_de_tres = {num for num in numeros if num % 3 == 0}
    pares_y_multiplos_de_tres = pares.intersection(multiplos_de_tres)

    print("Conjunto de pares:", pares)
    print("Conjunto de múltiplos de tres:", multiplos_de_tres)
    print("Intersección entre pares y múltiplos de tres:", pares_y_multiplos_de_tres)

# Uso de la función
encontrar_interseccion()
