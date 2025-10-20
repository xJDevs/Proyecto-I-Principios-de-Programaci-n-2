import random 

tipos_de_vehiculos = {

'Sedan': 3, 
'SUV': 3, 
'Ambulancia': 1, 
'Motocicleta': 2,
'Camion': 2,
'Policia': 1,
'Bomberos': 1,
'Bicicleta': 2 
}


def generador_lista_vehiculos(cantidad_vehiculos):

    combinaciones = []
    while True:
        try:
            cantidad_vehiculos = int(cantidad_vehiculos)
            break
        except:
            print('Por favor ingresar solamente numeros enteros!\n')
            continue

    for _ in range(cantidad_vehiculos):

        placa = random.randint(100000, 999999)
        hora = str(random.randint(0000, 2359)).zfill(4) # .zfill() rellena con 0's a la izquierda. Solo funciona con strings
        vehiculo = random.choice(list(tipos_de_vehiculos.keys())) # genera una lista con las keys del diccionario y obtiene un vehiculo random de la misma 
        prioridad = tipos_de_vehiculos[vehiculo]
        combinaciones.append([vehiculo, prioridad, placa, hora])

    return combinaciones


