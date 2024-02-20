

# lista = [8, 10, 7, 6, 9, 8, 5, 7]
# data una lista come questa l'algoritmo cerca la sottosequenza decrescente con somma degli elementi maggiore
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
    out_lista = []
    new_lista = []
    max_lista = []
    i = 0
    while i < len(lista):
        if len(out_lista) == 0:
            out_lista.append(lista[0])
        elif out_lista[-1] > lista[i]:
            out_lista.append(lista[i])
        elif out_lista[-1] < lista[i]:
            j = -1
            while j >= -len(out_lista):
                if out_lista[j] >= lista[i]:
                    # print(out_lista, ":", out_lista[j], ">=", lista[i])
                    if out_lista[j] == lista[i]:
                        new_lista.clear()
                        for x in out_lista[:j]:
                            new_lista.append(x)
                        for x in lista[i::]:
                            new_lista.append(x)
                        # print("given", out_lista, "till index j=",
                            # j, " and", lista, "from index i=", i)
                        # print(out_lista[:j])
                        # print("+", lista[i::])
                        if sum(max_lista) < sum(fun(new_lista)):
                            max_lista = fun(new_lista)
                        # print("---->", new_lista)
                        # fun(new_lista, count+1)
                    elif out_lista[j] > lista[i]:
                        sub_lista = new_lista
                        new_lista.clear()
                        for x in out_lista[:j+1]:
                            new_lista.append(x)
                        for x in lista[i::]:
                            new_lista.append(x)
                        # print(out_lista[:j+1])
                        # print("+", lista[i::])
                        if sum(max_lista) < sum(fun(new_lista)):
                            max_lista = fun(new_lista)
                        # print("---->", new_lista)

                elif len(new_lista) == 0:
                    for x in lista[i::]:
                        new_lista.append(x)
                        if sum(max_lista) < sum(fun(new_lista)):
                            max_lista = fun(new_lista)
                    # print("---->", new_lista)
                    fun(new_lista)
                j -= 1

        i += 1
    # print(count, "out: ", out_lista)
    if sum(out_lista) > sum(max_lista):
        return out_lista
    else:
        return max_lista


results = []
for y in range(22):
    mytxt = "input/input" + str(y)+".txt"
    file = open(mytxt, "r")
    text = file.readline()
    text = file.readline()
    prov = []
    lista_in = []
    prov = (text.strip()).split()
    for x in prov:
        lista_in.append(int(x))
    print("\nLista_in "+str(y)+": ", lista_in, "\n")

    lista_out = fun(lista_in)

    mytxt = "output/output" + str(y)+".txt"
    file = open(mytxt, "r")
    text = file.readline()
    text = file.readline()
    prov = []
    soluzione = []
    prov = (text.strip()).split()
    for x in prov:
        soluzione.append(int(x))
    print("\nsoluzione "+str(y)+": ", soluzione, "\n")

    print((str(y), lista_out == soluzione))
    results.append((str(y), lista_out == soluzione))
