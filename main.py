

import random 

placas = []

for i in range(2):
    placa = random.randint(100000, 999999)
    placas.append(placa)

print(placas, '\n')

hora_llegada = []

for i in range(2):
    hora = random.randint(0000, 2359)
    hora_llegada.append(str(hora).zfill(4))

print(hora_llegada, '\n')

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

tipos_de_carro = []

for i in range(2):
    vehiculo = random.choice(list(opciones.keys()))
    prioridad = opciones[vehiculo]
    tipos_de_carro.append([vehiculo, prioridad])

print(tipos_de_carro, '\n') 


combinaciones = []

for elemento in range(len(tipos_de_carro)):
    combinaciones.append([tipos_de_carro[elemento], placas[elemento], hora_llegada[elemento]])

print(combinaciones)

