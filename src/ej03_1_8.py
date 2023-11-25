def es_palindromo(palabra):

    if not isinstance(palabra, str):
        raise ValueError("La entrada debe ser una cadena.")

    palabra = palabra.lower()
    palabra_inversa = palabra[::-1]

    if palabra == palabra_inversa:
        print(f'La palabra "{palabra}" es un palíndromo.')
    else:
        print(f'La palabra "{palabra}" no es un palíndromo.')

palabra_usuario = input("Ingresa una palabra: ")
es_palindromo(palabra_usuario)

"""
palabra = pedir_palabra()

palabra_original = tuple (palabra)
                    (palabra)
palabra_alreves = [palabra]
palabra_alreves.reverse()
if palabra_original == palabra_alreves:
    print("Es un palindromo")
else:
    _________________________________
"""