'''
Clase:        1
Tema:         Bloque condicional
Ejercicio:    1
Descripción:  1.3.1. Automatizando el cálculo de la propina

Autor:        Enrique Hernández
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''

cuenta=int(input())
porcentaje_propina=int(input())
total_a_pagar=cuenta*((porcentaje_propina/100)+1)
print(total_a_pagar)