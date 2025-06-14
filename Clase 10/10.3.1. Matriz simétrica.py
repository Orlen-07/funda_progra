'''
Clase:        Clase 10
Tema:         Manejo de Matrices
Ejercicio:    2
Descripción:  10.3.1 Matriz simétrica

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
    fila=fila.split(",")
    for j in range(n): # Este for es para transformar los elementos de str a int
        fila[j]=int(fila[j])
    matriz.append(fila)

verificador=True
for i in range(1,n):
    for j in range(1,i+1):
        if matriz[i][i-j]==matriz[i-j][i]:
            continue
        else:
            verificador=False

if verificador==True:
    print("La Matriz es simétrica")
else:
    print("La Matriz no es simétrica")