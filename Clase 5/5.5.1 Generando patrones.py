'''
Clase:        5
Tema:         Estructuras Iterativas
Ejercicio:    3
Descripción:  5.5.1 Generando Patrones

Autor:        Enrique Hernández
Fecha:        2025-05-29
Estado:       [ Sin terminar ]
'''

print(3*" " + "+" + 3*" " + 2*"7")

for i in range(10):
    for j in range(3):
        if i<5 and i%2==0:
            print((2-j)*" " + ((2*j)+1)*"*" + (2-j)*" " + "_-_-_" + (2-j)*" " + ((2*j)+1)*"*" + (2-j)*" ")
        elif i<5 and i%2==1:
            print((j+1)*" " + ((2*j)+1)*"*" + "_-_-_" + (2-j)*" " + ((2*j)+1)*"*")