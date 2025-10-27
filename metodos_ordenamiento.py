# INSERTION SORT 
def insertion_sort(lista, index_ordenamiento):

    for i in range(1, len(lista)):
        valorActual = lista[i]
        j = i - 1

        while j >= 0 and lista[j][index_ordenamiento] > valorActual[index_ordenamiento]:
            lista[j + 1] = lista [j]
            j -=1
        lista[j + 1] = valorActual
    
    return lista


# BUBBLE SORT
def bubble_sort(lista, index_ordenamiento):

    copia = lista.copy()

    for pasada in range(len(copia) - 1):
        for valor in range(len(copia) - 1):
            if copia[valor][index_ordenamiento] > copia[valor + 1][index_ordenamiento]:
                temporal = copia[valor]
                copia[valor] = copia[valor + 1]
                copia[valor + 1] = temporal
    return copia


# SELECTION SORT 
def selection_sort(lista, index_ordenamiento):

    ordenada = []
    copia = lista.copy()

    while len(copia) > 0:
        valor_mas_pequeno = copia[0]
        for valor in copia:
            if valor[index_ordenamiento] < valor_mas_pequeno[index_ordenamiento]:
                valor_mas_pequeno = valor 
        ordenada.append(valor_mas_pequeno)
        copia.remove(valor_mas_pequeno)

    return ordenada


# QUICKSORT
def quicksort(lista, index_ordenamiento):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0] 
        menores = []
        iguales = []
        mayores = []
        
        for valor in lista:
            if valor[index_ordenamiento] < pivote[index_ordenamiento]:
                menores.append(valor)
            elif valor[index_ordenamiento] > pivote[index_ordenamiento]:
                mayores.append(valor)
            else:
                iguales.append(valor)
    ordenada = quicksort(menores, index_ordenamiento) + iguales + quicksort(mayores, index_ordenamiento)  # recursividad 
    
    return ordenada



# Ingresa a una lista los vehiculos de prioridad 1 y el resto lo acomoda con quicksort usando hora de llegada 
# Esta funciona mejor que todas excepto quicksort 

def metodo_rapido(lista, index_ordenamiento=None):
    lista_prioridad = []
    resto_de_listas = []

    for vehiculo in lista:
        if vehiculo[1] == 1:
            lista_prioridad.append(vehiculo)
        else:
            resto_de_listas.append(vehiculo)
    
    resto_ordenado = quicksort(resto_de_listas, 3)
    resultado = lista_prioridad + resto_ordenado
    return resultado


# Ordenamiento por Preclasifcacion de Prioridad 

def preclasificacion_por_prioridad(lista, index_ordenamiento=None):
    prioridades = {1: [], 2: [], 3: []}

    for vehiculo in lista:
        prioridades[vehiculo[1]].append(vehiculo)

    return prioridades[1] + prioridades[2] + prioridades[3]



