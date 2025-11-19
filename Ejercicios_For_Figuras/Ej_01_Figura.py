# Ejercicio de figura 1

altura = int(input("Escribe un número para determinar la altura de la figura: "))

print(" " * altura, end="")
print("*")
for i in range(1, altura + 1):
    print(" " * (altura - i), end="")
    print("*", end="")
    print(" " * (i - 1), end="")
    print("*")

for i in range(altura - 1, 0, -1):
    print(" " * (altura - i), end="")
    print("*", end="")
    print(" " * (i - 1), end="")
    print("*")
