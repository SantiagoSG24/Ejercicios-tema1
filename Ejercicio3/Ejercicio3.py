# Definir las dos listas de palabras
lista1 = ["manzana", "banana", "cereza", "durazno", "uva"]
lista2 = ["banana", "durazno", "kiwi", "manzana", "pera"]

# Generar la tercera lista con palabras que se repiten en ambas listas, sin repetición
lista3 = list(set(lista1) & set(lista2))

# Imprimir la tercera lista
print(lista3)