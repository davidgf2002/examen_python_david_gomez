def read_data(nombreFichero):
    linea = 1
    f = open(nombreFichero, mode="rt", encoding="utf-8")

    #leemos el fichero
    atributos = f.readline()
    #print("Leemos la primera linea: " + atributos)

    for linea in f:
        print(linea)

    f.close()