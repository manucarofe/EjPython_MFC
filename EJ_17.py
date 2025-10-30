# Ejercicio para pedir usuario y contraseña y verificar el inicio de sesión

usuario_guardado = "Betis"
contrasena_guardada = "caca"

print("Inicio de Sesión")

usuario_ingresado = input("Nombre de usuario: ")
contrasena_ingresada = input("Contraseña: ")

# El "and" se usa para hacer dos comparaciones VERDADERAS en un mismo condicional
if usuario_ingresado == usuario_guardado and contrasena_ingresada == contrasena_guardada:
    print("\n¡Inicio de sesión correcto!")
    print("¡Bienvenido, Betis!")
elif usuario_ingresado != usuario_guardado:
    print("\nError: Nombre de usuario incorrecto.")
else:
    print("\nError: Contraseña incorrecta.")