# Cadena de texto corrupta y al revés
cadena_corrupta = "sairolac 052 anetcer ed amohT"

# Voltear la cadena
cadena_volteada = cadena_corrupta[::-1]

# Separar la cadena en nombre de la receta y calorías
partes = cadena_volteada.split(' ', 1)
calorias = partes[0]
nombre_receta = partes[1]

# Formatear la cadena
resultado = f"La receta de {nombre_receta} contiene {calorias} calorías."

# Imprimir el resultado
print(resultado)