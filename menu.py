
from generador_cantidad_vehiculos import cantidad_de_vehiculos

def opciones_menu():

    valid = ('1', '2', '3', '4', '5')
    while True:
        opcion = input('Seleccione el metodo de ordenamiento que desea utilizar!\n' 
        '1. Bubble Sort 🫧 \n' 
        '2. Selection Sort 🎯 \n' 
        '3. Insertion Sort 🧩 \n' 
        '4. Quick Sort ⚡️ \n' 
        '5. Salir 👀 \n'
        '➡️: ')

        if opcion not in valid:
            print('Por favor seleccione una de las opciones disponibles del menu\n')
            continue
        break
    return opcion
        


while True:

    print('Bienvenido al menu de Ordenammiento Vehicular! 🚘')
    cantidad = input('Ingrese la cantidad de vehiculos que desea ordenar: \n --> ')
    
    lista_vehiculos = cantidad_de_vehiculos(cantidad)


    seleccion = opciones_menu()


    if seleccion == '1':
        print('Bubblesort')
    elif seleccion == '2':
        print('Selection sort')
    elif seleccion == '3':
        print('Insertion sort')
    elif seleccion == '4':
        print('Quicksort')
    else:
        print('Gracias por usar nuestro sistema de Ordenamiento Vehicular! 💻')
        break

