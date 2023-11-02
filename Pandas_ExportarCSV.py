import pandas as pd
import random
SEPARADOR = ("*" * 20) + "\n"

#Creacion de un DataFrame a partir de un diccionario
diccionario_notas_aleatorias = {\ 
    "Cresencio":[random.randrange(60,101) for x in range(3)], \
    "Domitila":[80,100,57], "Rutilio":[80,70,57], "Panfilo":[20,100,100], \
    "Ludoviko":[100,100,100]}
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programacion", "Base de datos", "Contabilidad"]


notas.to_csv (r'notas.csv',index=True, header=True) #No olvidar la extension del archivo
print("EXITO!")