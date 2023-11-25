import statistics

def estadisticas_muestra(muestra):
    
    if not isinstance(muestra, str):
        raise ValueError("La entrada debe ser una cadena.")

    numeros = [float(numero.strip()) for numero in muestra.split(',')]
    media = statistics.mean(numeros)
    desviacion_tipica = statistics.stdev(numeros)

    print(f"La media de la muestra es: {media}")
    print(f"La desviación típica de la muestra es: {desviacion_tipica}")

muestra_numeros = input("Ingrese una muestra de números separados por comas: ")
estadisticas_muestra(muestra_numeros)