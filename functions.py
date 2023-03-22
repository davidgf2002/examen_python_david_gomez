import csv

def read_data(nombreFichero):
    with open(nombreFichero, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)