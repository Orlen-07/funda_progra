'''
Clase:        5
Tema:         Estructuras Iterativas
Ejercicio:    2
Descripción:  5.4.2. Sumador de valores posicionales

Autor:        Enrique Hernández
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

num_str=input("Ingrese un número entero: ")
cont_digitos=len(num_str)
while cont_digitos>1:
    sum=0
    for i in num_str:
        sum=sum+int(i)
    num_str=str(sum)
    #print(num_str)         #esto lo use solo para probar que funcionará bien
    cont_digitos=len(num_str)
print(num_str)