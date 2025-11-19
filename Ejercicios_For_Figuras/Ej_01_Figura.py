# Ejercicio de figura 1

altura = int(input("Escribe un número para determinar la altura de la figura: "))

for i in range(altura):
    print(" " * i, altura,"*")
    altura + 1
    if altura == 0:
        print(" " * altura,"*"),"*"
        altura - 1
        if altura == 5:
            print("Ha completado la figura")