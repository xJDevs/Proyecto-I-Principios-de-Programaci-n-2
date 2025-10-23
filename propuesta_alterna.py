import time, textwrap
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

def agregar_tabla_txt(resultado):

    with open('/Users/johel/Desktop/Johel/TEC Johel/Progra 2/Proyecto 1/Proyecto-I-Principios-de-Programaci-n-2/tablas_comparativas.txt', 'a') as archivo:
        archivo.write(resultado)

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

    tabla = textwrap.dedent(f'''
    {'=' * 60}
    RESULTADOS DEL ORDENAMIENTO
    {'=' * 60}
    Método utilizado:     {nombre_metodo}
    Criterio:             {etiqueta_criterio}
    Vehículos ordenados:  {len(lista_vehiculos)}
    Tiempo de ejecución:  {tiempo_transcurrido:.6f} segundos
    {'=' * 60}
    ''')

    print(tabla)
    agregar_tabla_txt(tabla)

    print('\n📋 Lista de vehículos ordenados según el criterio seleccionado:\n')
    print(lista_ordenada)
    
    return tiempo_transcurrido, lista_ordenada

def ejecutar_menu_ordenamiento_vehicular():

    while True: 
        print('\nBienvenido al menú de Ordenammiento Vehicular! 🚘')

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
        
        medir_rendimiento_y_ordenar(
            funcion_ordenamiento, 
            lista_vehiculos,
            index_criterio,
            etiqueta_criterio,
            etiqueta_ordenamiento
        )
    
        repetir = soliciar_opcion_valida('\nDesea ordenar otra vez, una cantiad de vehiculos diferente?\n' \
        '1. Si\n'
        '2. No\n'
        '-->: ', 
        ('1','2'))
        if repetir != '1':
            print("Gracias por usar nuestro sistema de Ordenamiento Vehicular! 💻")
            break



ejecutar_menu_ordenamiento_vehicular()