def producto_matrices(matriz1, matriz2):
    
    if not all(isinstance(fila, list) for fila in matriz1) or not all(isinstance(fila, list) for fila in matriz2):
        raise ValueError("La entrada debe ser una lista anidada.")

    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    if columnas_matriz1 != filas_matriz2:
        print("Las matrices no tienen dimensiones compatibles para el producto.")
        return

    resultado = [[0 for _ in range(columnas_matriz2)] for _ in range(filas_matriz1)]

    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(filas_matriz2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    print("El producto de las matrices es:")
    for fila in resultado:
        print(fila)


# Ejemplo de uso
matriz_A = [[1, 2, 3], [4, 5, 6]]
matriz_B = [[-1, 0, 0], [1, 1, 1], [1, 0, 1]]
producto_matrices(matriz_A, matriz_B)