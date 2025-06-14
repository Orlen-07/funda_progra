# Crear una función que cuente recursivamente los vecinos en una matriz binaria

def contar(matriz):
    submatriz=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i==0:
                if j==0:
                    Mcontador=[matriz[i+1][j],matriz[i+1][j+1],matriz[i][j+1]]
                    contador=sum(Mcontador)
                elif j==len(matriz[0][-1])-1:
                    Mcontador=[matriz[i+1][j],matriz[i+1][j-1],matriz[i][j-1]]
                    contador=sum(Mcontador)
                else:
                    Mcontador=[matriz[i][j-1],matriz[i+1][j-1],matriz[i+1][j],matriz[i+1][j+1],matriz[i][j+1]]
                    contador=sum(Mcontador)
            if 