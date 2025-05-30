'''
Clase:        6
Tema:         Manejo de listas
Ejercicio:    1
Descripción:  6.2.1 Eliminando valores duplicados

Autor:        Enrique Hernández
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

numeros=input("Ingrese una lista de números separados por espacio: ")
numeros=numeros.split()
num=[]
for i in range((len(numeros))):
    num.append(int(numeros[i]))
num=set(num)
num_str=""
for x in num:
    num_str=num_str+str(x)+" "
print(num_str)