def load_file():
    filepath = input("Enter the path of the file to load: ")
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

my_file = load_file()

matriz = []
for line in my_file:
    fila = list(line.strip())
    fila = [int(char) for char in fila]
    matriz.append(fila)

def evaluar_casillas(i,j):
    if 0<i and i<len(matriz)-1 and 0<j and j<len(matriz[0])-1:
        sub_3x3=[matriz[i-1][j-1],matriz[i-1][j],matriz[i-1][j+1],matriz[i][j-1],matriz[i][j],matriz[i][j+1],matriz[i+1][j-1],matriz[i+1][j],matriz[i+1][j+1]]
        total_unos = sum(sum(fila) for fila in sub_3x3)
        return total_unos
    else:
        if i==0 and 0<j and j<len(matriz[0])-1:
            sub_3x3=[matriz[i][j-1],matriz[i][j],matriz[i][j+1],matriz[i+1][j-1],matriz[i+1][j],matriz[i+1][j+1]]
            total_unos = sum(sub_3x3)
            return total_unos
        elif i==len(matriz)-1 and 0<j and j<len(matriz[0])-1:
            sub_3x3=[matriz[i-1][j-1],matriz[i-1][j],matriz[i-1][j+1],matriz[i][j-1],matriz[i][j],matriz[i][j+1]]
            total_unos = sum(sub_3x3)
            return total_unos
        elif 0<i and i<len(matriz)-1 and j==0:
            sub_3x3=[matriz[i-1][j],matriz[i-1][j+1],matriz[i][j],matriz[i][j+1],matriz[i+1][j],matriz[i+1][j+1]]
            total_unos = sum(sub_3x3)
            return total_unos
        elif 0<i and i<len(matriz)-1 and j==len(matriz[0])-1:
            sub_3x3=[matriz[i-1][j-1],matriz[i-1][j],matriz[i][j-1],matriz[i][j],matriz[i+1][j-1],matriz[i+1][j]]
            total_unos = sum(sub_3x3)
            return total_unos
        else:
            if i==0 and j==0:
                sub_3x3=[matriz[0][1],matriz[]]
    

def juego_de_la_vida_de_Conway():
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==0:
                if fig_cont[i,j]<3 or fig_cont[i,j]>3:
                    continue
                else:
                    matriz[i][j]=1
            if matriz[i][j]==1:
                if fig_cont[i,j]==2 or fig_cont[i,j]==3:
                    continue
                else:
                    matriz[i][j]=0

gens=1000
for k in range(gens):
    contador_casillas_vivas()
    juego_de_la_vida_de_Conway()
    print(matriz)
