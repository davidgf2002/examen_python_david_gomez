import csv
import math
#type,fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality



def split(diccionario):
    #Dos diccionarios vacios para guardar los datos
    diccionarioWhite = {}
    diccionarioRed = {}

    #Se recorre el diccionario
    for type, row in diccionario.items():

        #Si el atributo type es "white", se añade al diccionarioWhite
        if(type == "White"):
            print("Blanco")
            diccionarioWhite.append(diccionario[row])

        #Si el atributo type es "red", se añade al diccionarioRed
        elif(type == "red"):
            print("Rojo")
            diccionarioRed.append(diccionario[row])

    return diccionarioRed, diccionarioWhite



def reduce(diccionario, atributo):
    #lista vacia para guardar los datos
    listaValores = []

    #Se recorre el diccionario
    for type, row in diccionario.items():
        #Si la clave coincide con el atributo que se pasa por parámetro, se añade a la lista su valor
        if type == atributo:
            listaValores.append(row)
            
    return listaValores




def silhouette(lista1, lista2):
    #lista que guardará los valores de S(i) para hacer la posterior media
    listaS = []


    #valores maximos de cada lista
    maximoLista1 = max(lista1)
    maximoLista2 = max(lista2)
    #FALTA COMPROBAR CUAL DE LOS DOS ES MAYOR


    #lista para A(i) y B(i)
    listaDistanciaA = []
    listaDistanciaB = []


    #Calcular b(i) -> Distancia lista1(i) y lista2
    for i in lista1:
        for j in lista2:
            aux = i - j
            distancia = math.sqrt(math.abs(math.pow(aux, 2)))
            distancia.append(listaDistanciaB)

    # FALTA CALCULAR MEDIA
    sumatorioB = 0
    mediaB = 0
    for i in listaDistanciaB:
        sumatorioB = sumatorioB + i

    mediaB = sumatorioB / len(listaDistanciaB)


    #Calcular a(i) -> Distancia lista1(i), resto lista1
    for i in lista1:
        aux = lista1[i] - lista1[i+1]
        distancia = math.sqrt(math.abs(math.pow(aux, 2)))
        distancia.append(listaDistanciaA)
        









'''
def read_data(nombreFichero):
    atributos = ["type","fixed" "acidity","volatile" "acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"]
    dict = []
    with open(nombreFichero, 'r') as file:
        reader = csv.reader(file)
        for row in reader:



        seating = []

        for i in range(self.__num_rows):
            row = {}
            for letter in seats:
                row[letter] = None #letter = clave, None = valor
                seating.append(row)
        seating = [ {letter: None for letter in seats} for i in range(self.__num_rows)]

        #seating = [ {letter: None for letter in seats} for i in range(self.__num_rows)]'''