# Programa que muestre los números pares comprendidos entre el 1 y el 200.

contador = 0
for i in range(0, 200, 1):
    contador += 1
    if i % 2 == 0:
        print(i)