def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError("El ítem ya está en el inventario")
    inventario.append(item)