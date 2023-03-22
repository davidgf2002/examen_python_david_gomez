import csv
#type,fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality

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

        #seating = [ {letter: None for letter in seats} for i in range(self.__num_rows)]


def split(diccionario):
    diccionarioWhite = {}
    diccionarioRed = {}

    for type, row in diccionario.items():
        if(type == "White"):
            print("Blanco")
            diccionarioWhite.append(diccionario[row])

        elif(type == "red"):
            print("Rojo")
            diccionarioRed.append(diccionario[row])