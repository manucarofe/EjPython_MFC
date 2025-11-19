# Ejercicio de figura 2

altura = int(input("Escribe un número para determinar la altura de la figura: "))

print("4")

for i in range(1, altura - 1):
    espacio = 2 * i - 1
    print("4", end="")
    print(" " * (espacio), end="")
    print("4")

print("4 " * altura, end="")