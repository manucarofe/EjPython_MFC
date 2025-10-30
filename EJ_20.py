# Ejercicio entre calificación numérica entre 0 y 10

try:
    nota = float(input("Ingrese una calificación numérica (0-10): "))

    if nota < 0 or nota > 10:
        print("Error: La calificación debe estar entre 0 y 10.")
    
    else:
        # Esto nos permite usar match para valores exactos.
        nota_entera = int(nota)
        
        calificacion = "" # Variable para guardar el resultado
        # | funciona para decir si es 0 "o" 1 "o" 2 
        match nota_entera:
            case 0 | 1 | 2:
                calificacion = "Muy Deficiente"
            
            case 3 | 4:
                calificacion = "Insuficiente"
            
            case 5:
                calificacion = "Suficiente"
            
            case 6:
                calificacion = "Bien"
            
            case 7 | 8:
                calificacion = "Notable"
            
            case 9 | 10:
                calificacion = "Sobresaliente"

        print(f"Calificación: {calificacion}")

except ValueError:
    print("Error: Por favor, ingrese un valor numérico.")
    