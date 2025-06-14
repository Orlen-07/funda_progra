'''
Clase:        Clase 10
Tema:         Manejo de Matrices
Ejercicio:    1
Descripción:  10.2.1. Diagonal principal y secundaria

Autor:        Enrique Hernández
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''

# Agarramos la cantidad de filas
n=int(input())

# Comenzamos a leer los datos y los guardamos en una matriz
matriz=[]
for i in range(n):
    fila=input()
    fila=fila.split(", ")
    for j in range(n): # Este for es para transformar los elementos de str a int
        fila[j]=int(fila[j])
    matriz.append(fila)

# Inicializo los arrays de las diagonales
diagonal1=[]
diagonal2=[]

# Agrego los elementos diagonales a cada array correspondiente
for i in range (n):
    diagonal1.append(matriz[i][i])
    diagonal2.append(matriz[i][n-i-1])

# Imprimo respuesta
print(diagonal1, diagonal2)