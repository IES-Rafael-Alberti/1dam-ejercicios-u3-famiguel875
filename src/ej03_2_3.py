def obtener_precio_fruta():
    precios_frutas = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
    fruta = input("Ingrese el nombre de la fruta: ")
    if fruta in precios_frutas:
        kilos = float(input("Ingrese el número de kilos: "))
        precio_total = precios_frutas[fruta] * kilos
        print(f"El precio de {kilos} kilos de {fruta} es: {precio_total} euros")
    else:
        print("La fruta no está en el diccionario.")

# Uso de la función
obtener_precio_fruta()