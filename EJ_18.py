# Ejercicio para pedir  número por teclado y decir si dicho número es múltiplo de 10

try:
    # Pedimos número por teclado
    num = int(input("Ingrese un número: "))

    # Lo que hace % es una división exacta y con el if de abajo comprobalos si es múltiplo o no
    if num % 10 == 0:
        print(f"El número {num} **sí** es múltiplo de 10.")
    else:
        print(f"El número {num} **no** es múltiplo de 10.")

except ValueError:
    print("Error: Por favor, ingrese solo un número entero.")