# Programa para calcular el interés compuesto
# Capital inicial
capital_inicial = 1000

# Leer la tasa de interés anual
tasa_interes = float(input("Introduce la tasa de interés anual (entre 1% y 10%): "))

# Validar que la tasa de interés esté en el rango correcto
if tasa_interes < 1 or tasa_interes > 10:
    print("La tasa de interés debe estar entre 1% y 10%.")
else:
    # Leer el número de años
    años = int(input("Introduce el número de años: "))

    # Calcular el interés compuesto
    tasa_interes /= 100  # Convertir la tasa de interés a decimal
    capital_final = capital_inicial * (1 + tasa_interes) ** años

    # Mostrar el capital final
    print(f"El capital final después de {años} años es: {capital_final:.2f}")