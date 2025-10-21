import time
from generador_cantidad_vehiculos import generador_lista_vehiculos
from metodos_ordenamiento import insertion_sort, bubble_sort, selection_sort, quicksort

METODOS_DE_ORDENAMIENTO = {
    "1": (bubble_sort, "Bubble Sort 🫧"),
    "2": (selection_sort, "Selection Sort 🎯"), 
    "3": (insertion_sort, "Insertion Sort 🧩"),
    "4": (quicksort, "Quick Sort ⚡️"),
    "5": (None, "Salir 👀")
}

CRITERIOS_DE_ORDEN = {
    "1": (1, "Prioridad 🚨"), 
    "2": (3, "Hora de llegada ⏰"),
    "3": (2, "Placa 🚗")
}

'''Se le pasa como parametro el texto que se desea imprimir y la lista de opciones validas'''
def soliciar_opcion_valida(texto, opciones_validas):
    while True:
        opcion = input(texto)
        if opcion in opciones_validas:
            return opcion
        print('Por favor seleccione una de las opciones validas del menu')

def solicitar_entero_positivo(texto):
    while True:
        cantidad = input(texto)
        if cantidad.isdigit() and int(cantidad) > 0:
            return int(cantidad)
        print("Por favor ingrese un numero entero positivo mayor a 0")

def mostrar_menu_criterio_y_obtener_seleccion():
    texto = ('=' * 60 + "\n"
        'Seleccione el criterio de ordenamiento:\n'
        '1. Prioridad 🚨\n'
        '2. Hora de llegada ⏰ \n'
        '3. Placa 🚗 \n'
        '➡️: '
    )
    opcion = soliciar_opcion_valida(texto, CRITERIOS_DE_ORDEN.keys())
    return CRITERIOS_DE_ORDEN[opcion]

def mostrar_menu_ordenamiento_y_obtener_seleccion():
    texto = ( '=' * 60 + "\n"
    'Seleccione el metodo de ordenamiento que desea utilizar:\n' 
    '1. Bubble Sort 🫧 \n' 
    '2. Selection Sort 🎯 \n' 
    '3. Insertion Sort 🧩 \n' 
    '4. Quick Sort ⚡️ \n' 
    '5. Salir 👀 \n'
    '➡️: '
    )

    opcion = soliciar_opcion_valida(texto, METODOS_DE_ORDENAMIENTO.keys())
    return METODOS_DE_ORDENAMIENTO[opcion]

def medir_rendimiento_y_ordenar(funcion_ordenamiento, lista_vehiculos, index_criterio, etiqueta_criterio, nombre_metodo):
    #Mide el tiempo de ejecucion de un metodo

    print(f'\n⏳ Ordenando {len(lista_vehiculos)} vehículos...')
    
    inicio = time.time()
    lista_ordenada = funcion_ordenamiento(lista_vehiculos, index_criterio)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    
    print('\n' + '=' * 60)
    print('RESULTADOS DEL ORDENAMIENTO')
    print('=' * 60)
    print(f'Método utilizado:     {nombre_metodo}')
    print(f'Criterio:             {etiqueta_criterio}')
    print(f'Vehículos ordenados:  {len(lista_vehiculos)}')
    print(f'Tiempo de ejecución:  {tiempo_transcurrido:.6f} segundos')
    print('=' * 60)
    
    return tiempo_transcurrido, lista_ordenada

def ejecutar_menu_ordenamiento_vehicular():

    print('Bienvenido al menú de Ordenammiento Vehicular! 🚘')

    cantidad_de_vehiculos = solicitar_entero_positivo('Ingrese la cantidad de vehiculos que desea ordenar: \n --> ')
    lista_vehiculos = generador_lista_vehiculos(cantidad_de_vehiculos)

    if not lista_vehiculos:
        print('No se pudieron generar los vehiculos. Intentelo de nuevo')
        return
    
    index_criterio, etiqueta_criterio = mostrar_menu_criterio_y_obtener_seleccion()
    funcion_ordenamiento, etiqueta_ordenamiento = mostrar_menu_ordenamiento_y_obtener_seleccion()

    if funcion_ordenamiento is None:
        print("Gracias por usar nuestro sistema de Ordenamiento Vehicular! 💻")
        return 
    
    tiempo_transcurrido, lista_ordenada = medir_rendimiento_y_ordenar(
        funcion_ordenamiento, 
        lista_vehiculos,
        index_criterio,
        etiqueta_criterio,
        etiqueta_ordenamiento
    )

    print('\n📋 Lista de vehículos ordenados según el criterio seleccionado:')
    print(lista_ordenada)

ejecutar_menu_ordenamiento_vehicular()