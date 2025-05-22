'''
Clase:        2
Tema:         Bloque condicional
Ejercicio:    2
Descripción:  2.3.2. Cálculo de impuesto

Autor:        Enrique Hernández
Fecha:        2025-05-21
Estado:       [ Terminado ]
'''

unidades_consumidas=int(input())
if unidades_consumidas<=100:
  print("Sin impuestos")
elif unidades_consumidas<=200:
  print(unidades_consumidas*0.5)
else:
  print(unidades_consumidas*0.7)