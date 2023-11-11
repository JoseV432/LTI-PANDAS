import pandas as pd
import random
SEPARADOR = ("*"  * 20) + "\n"

#Creación de un DataFrame a partir de un diccionario 
diccionario_notas_aleatorias = {\
   "Crescencio":[random.randrange(60,101) for x in range(3)], \
   "Domitila":[80,100,57], "Rutilio":[80,70,57], "Pánfilo":[20,100,100], \
   "Lodoviko":[100,100,100]}
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programación", "Base de datos", "Contabilidad"]


notas.to_csv (r'notas.csv',index=True, header=True) #No olvidar la extensión del archivo
print("ÉXITO!")