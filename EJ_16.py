# Ejercicio para pedir un número entre el 0 y el 99999 y decir cuantas cifras tiene

print("Escribe un número entre el 0 y el 99999")
num = input()

cantidad = 0
for i in num:
    cantidad = cantidad + 1
print("El número que has introducido tiene", cantidad, "cifras")