def producto_escalar(vector1, vector2):
    """
    Almacena los vectores en dos listas y muestra por pantalla su producto escalar.

    Parameters:
    - vector1 (tuple): Primer vector.
    - vector2 (tuple): Segundo vector.

    Raises:
    - ValueError: Si la entrada no es una tupla.

    Example:
    >>> producto_escalar((1, 2, 3), (-1, 0, 2))
    El producto escalar es: 5
    """
    if not isinstance(vector1, tuple) or not isinstance(vector2, tuple):
        raise ValueError("La entrada debe ser una tupla.")

    if len(vector1) != len(vector2):
        print("Los vectores deben tener la misma longitud.")
        return

    producto = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
    print(f"El producto escalar es: {producto}")

vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)
producto_escalar(vector1, vector2)