from functions import *


#Test read_data()
diccionarioReadData = {}
#diccionarioReadData = read_data("winequality.csv")
#print(diccionarioReadData)



#Test split()
diccionarioSplit1 = {}
diccionarioSplit2 = {}

diccionarioSplit1, diccionarioSplit2 = split(diccionarioReadData)
print(diccionarioSplit1)
print(diccionarioSplit2)



#Test reduce()
listaReduce1 = []
listaReduce2 = []

listaReduce1 = reduce(diccionarioSplit1)
listaReduce2 = reduce(diccionarioSplit2)
print(listaReduce1)
print(listaReduce2)



#Test silhouette()
coefSiolhouette = 0
coefSiolhouette = silhouette(listaReduce1, listaReduce2)

print(coefSiolhouette)