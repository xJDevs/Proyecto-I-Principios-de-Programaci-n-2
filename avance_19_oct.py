

import random 

# Definimos un diccionario para el tipo de vehículo y la prioridad que hemos elegido para cada uno 
opciones = {

'Sedan': 3, 
'SUV': 3, 
'Ambulancia': 1, 
'Motocicleta': 2,
'Camion': 2,
'Policia': 1,
'Bomberos': 1,
'Bicicleta': 2 
}

#Funcion para generar los vehículos y sus características aleatoriamente
def generar_vehiculos(cantidad):
    placas = [random.randint(100000, 999999) for _ in range(cantidad)]
    hora_llegada = [str(random.randint(0, 2359)).zfill(4) for _ in range(cantidad)]
    tipos_de_carro = [[tipo := random.choice(list(opciones.keys())), opciones[tipo]] for _ in range(cantidad)]

    combinaciones = []
    for i in range(cantidad):
        combinaciones.append([tipos_de_carro[i], placas[i], hora_llegada[i]])

    return combinaciones



#def selection_sort():
############

#def bubble_sort():
############


#método Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        valorActual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] >valorActual:
            lista[j + 1] = lista [j]
            j -=1
        lista[j + 1] = valorActual
    
    return lista






#Mensaje inicial de bienvenida
print('Bienvenido al menu de Ordenammiento Vehicular! 🚘')

try:
    cantidad = int(input('Ingrese la cantidad de vehiculos que desea ordenar: \n --> '))
    vehiculos = generar_vehiculos(cantidad)
except ValueError:
    print('Debe de ingresar un número válido')


def menu(opcion):
    match opcion:
        case 1:
            print('Selection sort')
        case 2:
            print('Bubblesort')
        case 3:
            print('Insertion sort')
            ordenados = insertion_sort(vehiculos)
            print('\nVehículos ordenados por prioridad (Insertion Sort):')
            for v in ordenados:
                print(v)
        case 4:
            print('Quicksort')
        case 5:
            print('Saliendo del programa')
            print('\nGracias por usar nuestro sistema de Ordenamiento Vehicular! 💻')
            exit()
        case _:
            print('Opción no válida')