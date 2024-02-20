


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
                    if out_lista[j] == lista[i]:
                        new_lista.clear()
                        for x in out_lista[:j]:
                            new_lista.append(x)
                        for x in lista[i::]:
                            new_lista.append(x)
                        if sum(max_lista) < sum(fun(new_lista)):
                            max_lista = fun(new_lista)
                    elif out_lista[j] > lista[i]:
                        sub_lista = new_lista
                        new_lista.clear()
                        for x in out_lista[:j+1]:
                            new_lista.append(x)
                        for x in lista[i::]:
                            new_lista.append(x)
                        if sum(max_lista) < sum(fun(new_lista)):
                            max_lista = fun(new_lista)

                elif len(new_lista) == 0:
                    for x in lista[i::]:
                        new_lista.append(x)
                        if sum(max_lista) < sum(fun(new_lista)):
                            max_lista = fun(new_lista)
                    fun(new_lista)
                j -= 1

        i += 1
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
    solution = []
    prov = (text.strip()).split()
    for x in prov:
        solution.append(int(x))
    print("\Solution "+str(y)+": ", solution, "\n")

    print((str(y), lista_out == solution))
    results.append((str(y), lista_out == solution))
