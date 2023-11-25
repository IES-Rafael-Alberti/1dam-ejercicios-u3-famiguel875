def obtener_domicilios_factura(compras):
    domicilios = set()
    for compra in compras:
        cliente, _, _, domicilio = compra
        domicilios.add(domicilio)
    return domicilios

# Ejemplo de uso
compras = [
    ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
    ("Jorge Russo", 7, 699, "Mirasol 218"),
    ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
    ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
    ("Jorge Russo", 15, 958, "Mirasol 218")
]

domicilios_factura = obtener_domicilios_factura(compras)
print("Domicilios para enviar la factura:", domicilios_factura)
