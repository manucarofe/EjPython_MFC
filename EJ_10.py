# Ejercicio contador con bucle for

print("Escribe un número entero: ")
num1 = input()
print("Escribe otro número entero(no puede ser cero): ")
num2 = input()
suma = num1 + num2
resta = num1 - num2
multiplicación = num1 * num2
if num2 == 0 :
    division = print("No se puede hacer porque el segundo número es un 0")
else:
    division= num1 / num2
    
print("El resultado de la suma es: ", suma)
print("El resultado de la resta es: ", resta)
print("El resultado de la multiplicación es: ", multiplicación)
print("El resultado de la división es: ", division)
