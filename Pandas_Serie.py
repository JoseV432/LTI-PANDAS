import numpy as np
import pandas as pd

SEPARADOR = ("*"  * 20) + "\n"

#Crear una serie con valores iniciales
notas = pd.Series([87, 100, 85, 60, 78])
print(type(notas))
print(notas)
print(SEPARADOR)



#Crear una serie de 6 elementos que tengan el mismo valor
iguales = pd.Series(100, range(6))
print(type(iguales))
print(iguales)
print(SEPARADOR)



#Estadísticas Descriptivas para una serie
print("notas :")
print(f"{notas}")
print(f"cantidad = {notas.count()}")
print(f"media = {notas.mean()}")
print(f"mínimo = {notas.min()}")
print(f"máximo = {notas.max()}")
print(f"desviación standard = {notas.std()}")
print(f"Sumarización descriptiva:")
print(notas.describe())
print(SEPARADOR)



#Serie con índices personalizados
print("Series con índices personalizados:")
notas_asignados = pd.Series([87, 100, 85, 60, 78], index=["Crescencio", "Domitila", "Rutilio", "Pánfilo", "Ludoviko"])

print(notas_asignados)
print(SEPARADOR)




print("Serie generada a partir de un diccionario")
notas_asignadas_dict = pd.Series({"Crescencio":87, "Domitila":100, "Rutilio":85, "Pánfilo":60, "Ludoviko":78})

print(notas_asignadas_dict)
print(SEPARADOR)





#Acceso a elementos en una serie por valor de índice
print(f"La calificación de Rutilio es {notas_asignadas_dict['Rutilio']}")
print(f"La calificación de Rutilio es {notas_asignadas_dict.Rutilio}")