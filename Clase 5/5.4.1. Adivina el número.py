'''
Clase:        5
Tema:         Estructuras Iterativas
Ejercicio:    1
Descripción:  5.4.1. Adivina el número

Autor:        Enrique Hernández
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''

import random

num_aleatorio=random.randint(1,100)

var_comparativa=0
print("Ingrese un número entero entre 1 y 100")

while num_aleatorio!=var_comparativa:
    num_ingresado=int(input())
    if num_ingresado==num_aleatorio:
        print("¡Acertaste! ¡Ese es el número que buscabas!: ", num_ingresado)
        break
    elif num_ingresado<num_aleatorio and num_ingresado>=1:
        print("El número que buscas es mayor que ", num_ingresado)
    elif num_ingresado>num_aleatorio and num_ingresado<=100:
        print("El número que buscas es menor que ", num_ingresado)
    else:
        print("Ingresa un número que este en el rango [1,100]")
    var_comparativa=num_ingresado