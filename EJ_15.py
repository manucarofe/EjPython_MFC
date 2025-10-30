# Ejercicio para saber cual es mayor, menor y si son iguales
numeros = []

print("Ingrese tres números enteros.")
for i in range(3):
    # Pedimos el número y lo convertimos a entero (int)
    num = int(input(f"Ingrese el número {i + 1}: "))
    # Lo añadimos a la lista
    numeros.append(num)

# Con max y min averiguamos cual es el mayor y cual el menor
mayor = max(numeros)
menor = min(numeros)

print("\nResultados")
print(f"La lista es: {numeros}")
print(f"El número **mayor** es: {mayor}")
print(f"El número **menor** es: {menor}")

# Comprobamos si son iguales
# Si el mayor y el menor son el mismo número, todos son iguales.
if mayor == menor:
    print("Los tres números son **iguales**.")
    
# Si no se cumple ninguno de los números son iguales
else:
    print("Todos los números son **diferentes**.")