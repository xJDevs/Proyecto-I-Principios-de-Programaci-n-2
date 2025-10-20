

carros = [['SUV', 3, '1320', 23455], ['Ambulancia', 1, '1640', 65243 ]]
index = 1



def insertion_sort(lista, index_ordenamiento):

    for i in range(1, len(lista)):
        valorActual = lista[i]
        j = i - 1

        while j >= 0 and lista[j][index_ordenamiento] > valorActual[index_ordenamiento]:
            lista[j + 1] = lista [j]
            j -=1
        lista[j + 1] = valorActual
    
    return lista


