'''
Clase:        Clase 10
Tema:         Manejo de Matrices
Ejercicio:    3
Descripción:  10.3.2. Juego del entorno

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

mat_resultante=[]

for i in range(n_filas):
    if (1<=i and i<n_filas-1):
        new_fila=[]
        for j in range(m_columnas):
            if (1<=j and j<m_columnas-1):
                submatriz=[matriz[i-1][j-1],matriz[i-1][j],matriz[i-1][j+1],matriz[i][j-1],matriz[i][j+1],matriz[i+1][j-1],matriz[i+1][j],matriz[i+1][j+1]]
                contador=sum(submatriz)
                new_fila.append(contador)
            elif j==0:
                submatriz=[matriz[i-1][j],matriz[i-1][j+1],matriz[i][j+1],matriz[i+1][j],matriz[i+1][j+1]]
                contador=sum(submatriz)
                new_fila.append(contador)
            elif j==m_columnas-1:
                submatriz=[matriz[i-1][j-1],matriz[i-1][j],matriz[i][j-1],matriz[i+1][j-1],matriz[i+1][j]]
                contador=sum(submatriz)
                new_fila.append(contador)
        mat_resultante.append(new_fila)
    elif i==0:
        new_fila=[]
        for j in range(m_columnas):
            if (1<=j and j<m_columnas-1):
                submatriz=[matriz[i][j-1],matriz[i][j+1],matriz[i+1][j-1],matriz[i+1][j],matriz[i+1][j+1]]
                contador=sum(submatriz)
                new_fila.append(contador)
            elif j==0:
                submatriz=[matriz[i][j+1],matriz[i+1][j],matriz[i+1][j+1]]
                contador=sum(submatriz)
                new_fila.append(contador)
            elif j==m_columnas-1:
                submatriz=[matriz[i][j-1],matriz[i+1][j-1],matriz[i+1][j]]
                contador=sum(submatriz)
                new_fila.append(contador)
        mat_resultante.append(new_fila)
    elif i==n_filas-1:
        new_fila=[]
        for j in range(m_columnas):
            if (1<=j and j<m_columnas-1):
                submatriz=[matriz[i-1][j-1],matriz[i-1][j],matriz[i-1][j+1],matriz[i][j-1],matriz[i][j+1]]
                contador=sum(submatriz)
                new_fila.append(contador)
            elif j==0:
                submatriz=[matriz[i-1][j],matriz[i-1][j+1],matriz[i][j+1]]
                contador=sum(submatriz)
                new_fila.append(contador)
            elif j==m_columnas-1:
                submatriz=[matriz[i-1][j-1],matriz[i-1][j],matriz[i][j-1]]
                contador=sum(submatriz)
                new_fila.append(contador)
        mat_resultante.append(new_fila)

print(mat_resultante)