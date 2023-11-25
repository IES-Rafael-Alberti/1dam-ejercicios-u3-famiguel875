def obtener_simbolo_divisa():
    diccionario_divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
    divisa = input("Ingrese una divisa: ")
    if divisa in diccionario_divisas:
        print(f"El símbolo de {divisa} es {diccionario_divisas[divisa]}")
    else:
        print("La divisa no está en el diccionario.")

# Uso de la función
obtener_simbolo_divisa()