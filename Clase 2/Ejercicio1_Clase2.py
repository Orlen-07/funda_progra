'''
Clase:        2
Tema:         Bloque condicional
Ejercicio:    1
Descripción:  2.3.1. Contraseña segura

Autor:        Enrique Hernández
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''

contra=input()
validador1=False
validador2=False
if len(contra)<8:
  print("La contraseña debe tener más de 7 caracteres")
else:
  for j in range(len(contra)):
    for i in range(10):
      if contra[j]==str(i):
        validador1=True
    if contra[j].isupper():
      validador2=True
if validador1==True and validador2==True:
  print("Contraseña válida")
else:
  print("Contraseña inválida")