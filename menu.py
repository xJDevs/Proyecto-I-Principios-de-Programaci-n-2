
from generador_cantidad_vehiculos import cantidad_de_vehiculos

def opciones_menu():

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
        
#se necesitaba seleccionar tambien el criterio de ordenamiento ademas del metodo, me parece que funciona bien por el momento
def seleccionar_criterio():
    valid = ('1', '2', '3')
    while True:
        print('=' * 60)
        criterio = input('Seleccione el criterio de ordenamiento:\n'
                         '1.Hora de llegada ⏰ \n'
                         '2.Prioridad 🚨\n'
                         '3.Tipo de vehiculo 🚗 \n '
                         '➡️: ')
        if criterio not in valid:
            print('Por favor, seleccione una de las opciones disponibles del menú\n')
            continue
        break
    return criterio

#falta funcion para medir rendimiento

print('Bienvenido al menú de Ordenammiento Vehicular! 🚘')

while True:
    while True:
        cantidad = input('Ingrese la cantidad de vehiculos que desea ordenar: \n --> ')
        if cantidad.isdigit() and int(cantidad) >0:
            cantidad = int(cantidad)
            break
        else:
            print('Por favor ingrese un numero valido mayor a 0\n')
            
    
    lista_vehiculos = cantidad_de_vehiculos(cantidad)
    if not lista_vehiculos:
        print('No se pudieron generar los vehiculos, intente nuevamente\n')
        continue

    criterio= seleccionar_criterio()


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

