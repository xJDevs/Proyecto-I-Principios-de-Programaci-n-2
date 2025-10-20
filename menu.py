import time
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

    return index_lista, criterio

def medir_rendimiento(funcion_ordenamiento, lista, index_ordenamiento, critero_texto, nombre_metodo):
    #Mide el tiempo de ejecucion de un metodo

    print(f'\n⏳ Ordenando {len(lista)} vehículos...')
    
    inicio = time.time()
    resultado = funcion_ordenamiento(lista, index_ordenamiento)
    fin = time.time()
    
    tiempo_transcurrido = fin - inicio
    
    criterios_nombres = {
        '1': 'Hora de llegada ⏰',
        '2': 'Prioridad 🚨',
        '3': 'Placa 🚗'
    }
    
    print('\n')
    print('=' * 60)
    print('RESULTADOS DEL ORDENAMIENTO')
    print('=' * 60)
    print(f'Método utilizado:     {nombre_metodo}')
    print(f'Criterio:             {criterios_nombres[criterio_texto]}')
    print(f'Vehículos ordenados:  {len(lista)}')
    print(f'Tiempo de ejecución:  {tiempo_transcurrido:.6f} segundos')
    print('=' * 60)
    
    return tiempo_transcurrido, resultado

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

    index_ordenamiento, criterio_texto = seleccionar_criterio()
    seleccion = menu_principal()


    if seleccion == '1':
        tiempo, ordenada = medir_rendimiento(bubble_sort,lista_vehiculos, index_ordenamiento, criterio_texto,'Bubble Sort 🫧' )
        break
    elif seleccion == '2':
        tiempo, ordenada = medir_rendimiento(selection_sort,lista_vehiculos, index_ordenamiento, criterio_texto,'Selection Sort 🎯')
        break
    elif seleccion == '3':
        tiempo, ordenada = medir_rendimiento(insertion_sort,lista_vehiculos, index_ordenamiento, criterio_texto,'Insertion Sort 🧩')
        break
    elif seleccion == '4':
        tiempo, ordenada = medir_rendimiento(quicksort,lista_vehiculos, index_ordenamiento, criterio_texto,'Quick Sort ⚡️')
        break
    else:
        print('Gracias por usar nuestro sistema de Ordenamiento Vehicular! 💻')
        break
print('\n📋 Lista de vehículos ordenados según el criterio seleccionado:')

print(ordenada)


