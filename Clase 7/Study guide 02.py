'''
Clase:        Clase 7
Tema:         Introducción a Numpy
Ejercicio:    Guía de Trabajo 2
Descripción:  2. Caso de Estudio: Consumo Energético

Autor:        Enrique Hernández
Fecha:        2025-06-02
Estado:       [ Terminado ]
'''


import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])


#Exploración inicial de los datos
print("Dimensiones: ", consumo.ndim)
print("Forma: ", consumo.shape)
print("Tipo de datos: ", consumo.dtype)
print("Consumo primer hogar: ", consumo[0])
print("Consumo el miercoles (día 3): ", consumo[:,3])


# Promedio de consumo por hogar
promedio_por_hogar = np.mean( consumo, axis=1)
# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)
# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)
print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)


# Maximo por hogar
maximos = np.max(consumo, axis=1)
# Minimo por dia15
minimos = np.min(consumo, axis=0)
# Desviación estándar global
desviacion= np.std(consumo)
print(maximos)
print(minimos)
print(desviacion)


# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
# Indice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
# Indice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)
print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)


# Suma por hogar ( semana )
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")
# Compara cada hogar con un valor mayera 100
altos = consumo_total_hogar > 100
# Filtrando hogares que cumplen la condtcidn:
consumo_mayor_100 = np.where(altos)[0]
print(f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")


# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min())/(consumo.max()-consumo.min())
# Resultado
print(consumo_normalizado)


#####################################################################################


# Tarea

# 1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
print(consumo[4,4])

# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
indices=[-3,-2,-1]
print(consumo[indices,-1])

# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
promedio=np.sum(consumo[:,-2] + consumo[:,-1])/20
print(promedio)

# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
dias_num={
    0: "Lunes",
    1: "Martes",
    2: "Miercoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sabado",
    6: "Domingo"
}
desviaciones=[]
for i in range(consumo.shape[1]):
    desviaciones.append(np.std(consumo[:,i]))
desv_max=np.max(desviaciones)
for j in range(len(desviaciones)):
    if desviaciones[j]==desv_max:
        print(f"El día con la mayor desviación es: {dias_num[j]}")
        print(f"Esto implica que {dias_num[j]} es el día que más varia el consumo de energía en los hogares")
        break
    else:
        continue

# 5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
pos={
    0: "primer",
    1: "segundo",
    2: "tercer"
}
resp=[]
consumoth=consumo_total_hogar.copy()
consumoth.sort()
print(consumoth)
for i in range(3):
    print(f"El {pos[i]} hogar con menor consumo de energía durante la semana es: {np.where(consumo_total_hogar==consumoth[i])[0][0]} con {consumoth[i]}")

# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
suma_h3=0
for i in consumo[2]:
    suma_h3=suma_h3+consumo[2,0]*(1+(i/10))
print(f"Si el hogar 3 aumenta su consumo un 10% cada día con respecto al primer día, entonces su nuevo consumo semanal es: {suma_h3}")
