from generador_cantidad_vehiculos import cantidad_de_vehiculos
from metodos_ordenamiento import insertion_sort, bubble_sort, selection_sort, quicksort

def menu_principal():

    valid = ('1', '2', '3', '4', '5')
    while True:
        print('=' * 60)
        opcion = input('Seleccione el metodo de ordenamiento que desea utilizar:\n' 
        '1. Bubble Sort 🫧 \n' 
        '2. Selection Sort 🎯 \n' 
        '3. Insertion Sort 🧩 \n' 
        '4. Quick Sort ⚡️ \n' 
        '5. Salir 👀 \n'
        '➡️: ')

        if opcion not in valid:
            print('Por favor seleccione una de las opciones disponibles del menú\n')
            continue
        break
    return opcion
        
# Se necesitaba seleccionar tambien el criterio de ordenamiento ademas del metodo, me parece que funciona bien por el momento
def seleccionar_criterio():
    valid = ('1', '2', '3')
    index_lista = None 
    while True:
        print('=' * 60)
        criterio = input('Seleccione el criterio de ordenamiento:\n'
                         '1.Prioridad 🚨\n'
                         '2.Hora de llegada ⏰ \n'
                         '3.Placa 🚗 \n'
                         '➡️: ')
        if criterio not in valid:
            print('Por favor seleccione una de las opciones disponibles del menú\n')
            continue
        break

    if criterio == '1':
        index_lista = 1
    elif criterio == '2':
        index_lista = 3
    else:
        index_lista = 2

    return index_lista

#falta funcion para medir rendimiento

print('Bienvenido al menú de Ordenammiento Vehicular! 🚘')

while True:
    while True:
        cantidad = input('Ingrese la cantidad de vehiculos que desea ordenar: \n --> ')
        if cantidad.isdigit() and int(cantidad) > 0:
            cantidad = int(cantidad)
            break
        else:
            print('Por favor ingrese un numero entero valido mayor a 0\n')
            
    lista_vehiculos = cantidad_de_vehiculos(cantidad)

    if not lista_vehiculos:
        print('No se pudieron generar los vehiculos, intente nuevamente\n')
        continue

    criterio = seleccionar_criterio()
    seleccion = menu_principal()


    if seleccion == '1':
        ordenada = bubble_sort(lista_vehiculos, criterio)
        break
    elif seleccion == '2':
        ordenada = selection_sort(lista_vehiculos, criterio)
        break
    elif seleccion == '3':
        ordenada = insertion_sort(lista_vehiculos, criterio)
        break
    elif seleccion == '4':
        ordenada = quicksort(lista_vehiculos, criterio)
        break
    else:
        print('Gracias por usar nuestro sistema de Ordenamiento Vehicular! 💻')
        break

print(ordenada)


