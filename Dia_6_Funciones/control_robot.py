def decision (distancia):
    if distancia < 15:
        return'detener'
    elif distancia < 30:
        return 'reduciendo velocidad'
    else:
        return 'Avanzar'

sensores = []

for i in range (3):
    try :
        valor = float(input('Digite valores del sensor: '))
        sensores.append(valor)
        print (sensores)
    except ValueError :
        print('Porfavor ingrese un valor valido')
        exit()

        
print('Valores ingresados en sensores: ', sensores)

print('Decision tomada basada en los sensores: ')

for distancia in sensores :
    print('Distancia:', distancia, 'cm ', decision(distancia))    