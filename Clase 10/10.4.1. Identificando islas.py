'''
Clase:        Clase 10
Tema:         Manejo de Matrices
Ejercicio:    4
Descripción:  10.4.1. Identificando islas

Autor:        Enrique Hernández
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''

n_filas=int(input())
m_columnas=int(input())

matriz=[]

for i in range(n_filas):
    fila=input()
    fila=fila.split(",")
    for j in range(len(fila)): # Este for es para transformar los elementos de str a int
        fila[j]=int(fila[j])
    matriz.append(fila)

contador=0

for i in range(n_filas):
    for j in range(m_columnas):
        if i==0 and j==0:
            if matriz[i][j]==1:
                contador=contador+1
        elif i==0 and j>0:
            if matriz[i][j]==1:
                if matriz[i][j-1]==0:
                    contador=contador+1
        elif i>0 and j==0:
            if matriz[i][j]==1:
                if matriz[i-1][j]==0:
                    contador=contador+1
        else:
            if matriz[i][j]==1:
                if matriz[i-1][j]==0 and matriz[i][j-1]==0:
                    contador=contador+1

print(contador)