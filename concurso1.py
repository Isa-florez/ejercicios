# Si acierto, mostrar “¡Correcto!”.
# Si no, mostrar “Intenta otra vez” y seguir hasta acertar.
# Concurso "Adivina el número secreto"

import random

numero_secreto = random.randint(1, 5)

intento = 0

while intento != numero_secreto:
    
    intento = int(input("Adivina el número (entre 1 y 5): "))

    if intento == numero_secreto:
        print("¡Correcto! ")
    else:
        print("Intenta otra vez ")