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
    #Se inicializa el mayor, como uno de los dos anteriores
    mayor = maximoLista1
    #Se comprueba si el maximo de la lista2 es mayor que el de la lista1
    if(maximoLista2 > mayor):
        mayor = maximoLista2


    #lista para A(i) y B(i)
    listaDistanciaA = []
    listaDistanciaB = []


    #Calcular b(i) -> Distancia lista1(i) y lista2
    for i in lista1:
        for j in lista2:
            aux = i - j
            distancia = math.sqrt(abs(math.pow(aux, 2)))
            listaDistanciaB.append(distancia)

    #Media b(i)
    sumatorioB = 0
    mediaB = 0
    for i in listaDistanciaB:
        sumatorioB = sumatorioB + i

    mediaB = sumatorioB / len(listaDistanciaB)




    #Calcular a(i) -> Distancia lista1(i), resto lista1
    for i in range(0, len(lista1)-1):
        aux = lista1[i] - lista1[i+1]
        distancia = math.sqrt(abs(math.pow(aux, 2)))
        listaDistanciaA.append(distancia)


    #Media a(i)
    sumatorioA = 0
    mediaA = 0
    for i in listaDistanciaA:
        sumatorioA = sumatorioA + i

    mediaA = sumatorioA / len(listaDistanciaA)




    #Se calcula S y se añade a la lista final
    valorS = (mediaB - mediaA)/(mayor)
    listaS.append(valorS)


    #Se calcula el coeficiente de Silhouette
    sumatorioSilhouette = 0
    for i in listaS:
        sumatorioSilhouette = sumatorioSilhouette + i
    

    #Se devuelve el coeficiente de Silhouette (sumatorio/longitud)
    return sumatorioSilhouette / len(listaS)









def read_data(nombreFichero):
    atributos = ["type","fixed" "acidity","volatile" "acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"]
    dict = {}
    with open(nombreFichero, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
        
            for i in atributos:
                row = {}
        
