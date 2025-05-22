unidades_consumidas=int(input())
if unidades_consumidas<=100:
  print("Sin impuestos")
elif unidades_consumidas<=200:
  print(unidades_consumidas*0.5)
else:
  print(unidades_consumidas*0.7)