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
        hora = f'{random.randint(0, 23):random.randint(0, 59)}' 
        vehiculo = random.choice(list(tipos_de_vehiculos.keys())) # genera una lista con las keys del diccionario y obtiene un vehiculo random de la misma 
        prioridad = tipos_de_vehiculos[vehiculo]
        combinaciones.append([vehiculo, prioridad, placa, hora])

    return combinaciones


valid_ranges = [
    (0, 60),     # 0000–0060
    (100, 160),  # 0100–0160
    (200, 260),  # 0200–0260
    (300, 360),
    (400, 460),
    (500, 560),
    (600, 660),
    (700, 760),
    (800, 860),
    (900, 960),
    (1000, 1060),
    (1100, 1160),
    (1200, 1260),
    (1300, 1360),
    (1400, 1460),
    (1500, 1560),
    (1600, 1660),
    (1700, 1760),
    (1800, 1860),
    (1900, 1960),
    (2000, 2060),
    (2100, 2160),
    (2200, 2260),
    (2300, 2359)  # último rango
]