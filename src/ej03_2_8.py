def traducir_frase():
    diccionario_traduccion = {}

    # Ingresar palabras y traducciones
    entrada = input("Ingrese palabras y traducciones en formato palabra:traduccion, separados por coma: ")
    pares = [par.split(':') for par in entrada.split(',')]
    diccionario_traduccion = dict(pares)

    # Traducir una frase
    frase = input("Ingrese una frase en español: ")
    palabras = frase.split()
    traduccion = [diccionario_traduccion.get(palabra, palabra) for palabra in palabras]
    print("Traducción:", ' '.join(traduccion))

# Uso de la función
traducir_frase()
