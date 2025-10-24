from generador_cantidad_vehiculos import generador_lista_vehiculos
#  INSERTION SORT 
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


########################################

# Este funciona mejor que todas excepto quicksort 

def metodo_rapido(lista, index_ordenamiento=None):
    lista_prioridad = []
    resto_de_listas = []

    for vehiculo in lista:
        if vehiculo[1] == 1:
            lista_prioridad.append(vehiculo)
        else:
            resto_de_listas.append(vehiculo)
    
    resto_ordenado = quicksort(resto_de_listas, 2)
    resultado = lista_prioridad + resto_ordenado
    return resultado

# este revienta a todas jaja

def preclasificacion_por_prioridad(lista, index_ordenamiento=None):
    prioridades = {1: [], 2: [], 3: []}

    for vehiculo in lista:
        prioridades[vehiculo[1]].append(vehiculo)

    return prioridades[1] + prioridades[2] + prioridades[3]

# este funciona mejor porque es lineal. a diferencia de los otros algoritmos, este metodo no compara, no cambia posiciones, no ve valores vecinos, solamente clasifica y agrega a una lista cuando cumple la condicion que queremos. esto tiene una explicacion, aun no lo comprendo mucho (tiene que ver con algo que se llama "Big O Notation"), pero basicamente se debe a como crecen la cantidad de operaciones que hace un algoritmo en base a la cantidad de comparaciones que tiene ue hacer, es decir, se multiplican la cantidad de operaciones al cuadrado, conforme crece el agoritmo. Este metodo al ordenar de manera lineal, no crece exponencialmente: si hay 1000 datos a clasificar, clasifica 1000 datos y punto 



