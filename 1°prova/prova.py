
# lista = [8, 10, 7, 6, 9, 8, 5, 7]
# data una lista come questa l'algoritmo cerca la sotto-sequenza decrescente con somma degli elementi maggiore
# [8, 7, 6, 5]
# [8, 7]
# [8]
# [10, 7, 6, 5]
# [10, 7]
# [10, 9, 8, 7]
# [10, 8, 5]
# [10, 8, 7]
# Si può rendere più efficiente valutando meno liste


def fun(lista):
    



for y in range(22):
    mytxt = "/Users/anaslaknitri/Desktop/python-workplace/1°prova/input/input" + \
        str(y)+".txt"
    file = open(mytxt, "r")
    text = file.readline()
    text = file.readline()
    prov = []
    lista_in = []
    prov = (text.strip()).split()
    for x in prov:
        lista_in.append(int(x))
    # print("\nLista_in "+str(y)+": ", lista_in, "\n")

    lista_out = fun(lista_in)

    mytxt = "/Users/anaslaknitri/Desktop/python-workplace/1°prova/output/output" + \
        str(y)+".txt"
    file = open(mytxt, "r")
    text = file.readline()
    text = file.readline()
    prov = []
    soluzione = []
    prov = (text.strip()).split()
    for x in prov:
        soluzione.append(int(x))
    # print("\nsoluzione "+str(y)+": ", soluzione, "\n")

    print(lista_out == soluzione)
    # results.append((str(y), lista_out == soluzione))
