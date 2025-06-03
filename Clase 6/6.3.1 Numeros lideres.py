'''
Clase:        6
Tema:         Manejo de listas
Ejercicio:    2
Descripción:  6.3.1 Números líderes

Autor:        Enrique Hernández
Fecha:        2025-06-02
Estado:       [ Terminado ]
'''

lstr=input("Introduzca una lista números separados por espacio: ")
lstr=lstr.split()
list=[]
for i in range(len(lstr)): list.append(int(lstr[i]))
lon=len(list)-1
resp=[]
for i in range(lon):
    validador=True
    for j in range(i+1,lon+1):
        if list[i]>list[j]:
            continue
        else:
            validador=False
            break
    if validador==True:
        resp.append(list[i])
for i in resp:
    print(str(i), end=" ")
print("")