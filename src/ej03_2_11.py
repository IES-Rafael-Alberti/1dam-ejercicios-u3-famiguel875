def parsear_directorio(clientes_str):
    lineas = clientes_str.strip().split('\n')
    campos = lineas[0].split(';')
    clientes = {}

    for linea in lineas[1:]:
        valores = linea.split(';')
        cliente = {}
        for i in range(len(campos)):
            campo = campos[i]
            valor = valores[i]
            if campo == 'descuento':
                valor = float(valor)
            cliente[campo] = valor
        nif = cliente['nif']
        clientes[nif] = cliente

    return clientes

# Ejemplo de uso
clientes_str = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
clientes_diccionario = parsear_directorio(clientes_str)
print(clientes_diccionario)
