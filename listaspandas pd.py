import pandas as pd
import random
SEPARADOR = ("*" * 20) + "\n"

#Creacion de un DataFrame a partir de un diccionario
diccionario_notas_aleatorias = {\
    "Cresencio":[random.randrange(60,101) for x in range(3)], \
    "Domitila":[80,100,57], "Rutillo":[80,70,57], "Panfilo":[20,100,100], \
    "Ludoviko":[100,100,100]}
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programacion", "Base de datos", "Contabilidad"]

#Accesar renglones utilizando slices
#Importante:En este formato, el final del slice SI esta incluido
print("Todas las asignaturas, todos los estudiantes")
subConjunto = notas.loc["Programacion":"Contabilidad"]
print(subconjunto)
x = input("Presiona una tecla")


print(SEPARADOR)

print("Ultimas dos asignturas, todos los estudiantes")
subConjunto = notas.loc["Base de datos":"Contabilidad"]
print(subConjunto)
print(SEPARADOR)

#Accesar subconjuntos de renglones y columnas
print("Subconjunto, solamente las notas de Rutillo y Ludoviko para las primeras dos asignaturas")
subConjunto = notas.loc["Programacion":"Base de datos", ["Rutillo","Ludoviko"]]
print(subConjunto)
print(SEPARADOR)

#Indexado booleano
print("Solamente calificaciones aprobatorias")
aprobados = notas[notas >= 70]
print(aprobados)
print(SEPARADOR)

print("Solamente calificaciones aprobatorias entre 70 y 80")
aprobados = notas[(notas >= 70) & (notas <= 80)]   #DEBE utilizarse &
print(aprobados)
print(SEPARADOR)

print("Solamente calificaciones NO aprobatorias que sean pares")
reprobadas_pares = notas[(notas <= 70) & (notas % 2 == 0)]
print(reprobados_pares)
print(SEPARADOR)

