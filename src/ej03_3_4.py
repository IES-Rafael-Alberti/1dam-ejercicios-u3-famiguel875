def comparar_frutas():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)

    frutas_comunes = set_frutas1.intersection(set_frutas2)
    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1

    print("Frutas comunes:", frutas_comunes)
    print("Frutas solo en frutas1:", frutas_solo_en_frutas1)
    print("Frutas solo en frutas2:", frutas_solo_en_frutas2)

# Uso de la función
comparar_frutas()
