# Ejercicio círculo

pi = 3.14159
radio = float(input("Introduce la longitud del radio: "))
circunferencia = 2 * pi * radio
area = pi * (radio ** 2)
volumen = (4 / 3) * pi * (radio ** 3)

# Mostramos todos los resultados
print("\n--- Resultados ---")
print("Longitud de la circunferencia:", circunferencia)
print("Área del círculo:", area)
print("Volumen de la esfera:", volumen)