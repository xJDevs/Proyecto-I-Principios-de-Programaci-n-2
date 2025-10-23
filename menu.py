import time, textwrap
from generador_cantidad_vehiculos import generador_lista_vehiculos
from metodos_ordenamiento import insertion_sort, bubble_sort, selection_sort, quicksort

def agregar_tabla_txt(resultado):

    with open('/Users/johel/Desktop/Johel/TEC Johel/Progra 2/Proyecto 1/Proyecto-I-Principios-de-Programaci-n-2/tablas_comparativas.txt', 'a') as archivo:
        archivo.write(resultado)

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
                         '1. Prioridad 🚨\n'
                         '2. Hora de llegada ⏰ \n'
                         '3. Placa 🚗 \n'
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
        '1': 'Prioridad 🚨',
        '2': 'Hora de llegada ⏰',
        '3': 'Placa 🚗'
    }
    
    tabla = textwrap.dedent(f'''
    {'=' * 60}
    RESULTADOS DEL ORDENAMIENTO
    {'=' * 60}
    Método utilizado:     {nombre_metodo}
    Criterio:             {criterios_nombres[criterio_texto]}
    Vehículos ordenados:  {len(lista)}
    Tiempo de ejecución:  {tiempo_transcurrido:.6f} segundos
    {'=' * 60}
    ''')

    print(tabla)
    agregar_tabla_txt(tabla)

    print('📋 Lista de vehículos ordenados según el criterio seleccionado:\n')
    print(resultado)
    
    return tiempo_transcurrido, resultado

print('\nBienvenido al menú de Ordenammiento Vehicular! 🚘')

while True:
    while True:
        cantidad = input('Ingrese la cantidad de vehiculos que desea ordenar: \n --> ')
        if cantidad.isdigit() and int(cantidad) > 0:
            cantidad = int(cantidad)
            break
        else:
            print('Por favor ingrese un numero entero valido mayor a 0\n')
            
    lista_vehiculos = generador_lista_vehiculos(cantidad)

    if not lista_vehiculos:
        print('No se pudieron generar los vehiculos, intente nuevamente\n')
        continue

    index_ordenamiento, criterio_texto = seleccionar_criterio()
    seleccion = menu_principal()


    if seleccion == '1':
        tiempo, ordenada = medir_rendimiento(bubble_sort,lista_vehiculos, index_ordenamiento, criterio_texto,'Bubble Sort 🫧' )
    elif seleccion == '2':
        tiempo, ordenada = medir_rendimiento(selection_sort,lista_vehiculos, index_ordenamiento, criterio_texto,'Selection Sort 🎯')
    elif seleccion == '3':
        tiempo, ordenada = medir_rendimiento(insertion_sort,lista_vehiculos, index_ordenamiento, criterio_texto,'Insertion Sort 🧩')
    elif seleccion == '4':
        tiempo, ordenada = medir_rendimiento(quicksort,lista_vehiculos, index_ordenamiento, criterio_texto,'Quick Sort ⚡️')
    else:
        print('Gracias por usar nuestro sistema de Ordenamiento Vehicular! 💻')
        break

    repetir = input('\nDesea ordenar otra vez, una cantiad de vehiculos diferente?\n' \
    '1. Si\n'
    '2. No\n'
    '-->: ')
    print()

    if repetir != '1':
        print('Gracias por usar nuestro sistema de Ordenamiento Vehicular! 💻')
        break




