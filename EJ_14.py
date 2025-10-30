# Ejercicio para saber si es mayor o son iguales

print("Escribe un número: ")
num1 = input()
print("Escribe el segundo número: ")
num2 = input()
if num1 == num2:
    print("Los números introducidos son iguales")
elif num1 > num2:
    print("El primer número es el mayor: ", num1)
else:
    print("El segundo número es el mayor: ", num2)
