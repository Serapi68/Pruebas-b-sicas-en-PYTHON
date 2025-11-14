def obstaculos (sensores): #Programacion de maniobra de esquive
    umbral = 15

    frente = sensores.get('frente', 100)
    izquierda = sensores.get('izquierda', 100)
    derecha = sensores.get('derecha', 100)
    
    if frente < umbral:
        if izquierda >= umbral:
            return 'Obstáculo al frente. Girar a la izquierda.'
        elif derecha >= umbral:
            return 'Obstáculo al frente. Girar a la derecha.'
        else:
            return 'Obstáculo en todas las direcciones. Detener robot.'
    else:
        return 'Camino despejado. Avanzar robot.'


#programacion de diccionario de robot

robot = {'nombre': input('Digite nombre: ').capitalize(),
          'bateria': 75,
          'Velocidad': 5.0 }

print('Valores principales: ')
for clave in robot:
    print(clave, ':', robot[clave])

robot['bateria'] = 65


#Elige modo del robot

while True:
    try:
        x = int(input('Elige el modo de operar el robot 1=Patrulla, 0=Reconocimiento, 2=Manual: '))
        if x == 1 :
            robot['modo'] = 'Patrulla' 
            print(robot['modo'])
            break
        elif x == 2 :
            robot ['modo'] = 'Manual'
            print(robot['modo'])
            break
        elif x== 0 :
            robot ['modo'] = 'Reconocimiento' 
            print(robot['modo'])
            break
        else:
            print('Ingrese un valor valido(0, 1, 2)')
    except ValueError :
        print('Porfavor ingrese un valor valido')

#Control de sensores

print('Digite lectura de sensores: ')
sensores ={'frente': int(input('Distancia de frente en cm: ')),
           'izquierda': int(input('Distancia de izquierda en cm: ')),
           'derecha': int(input('Distancia derecha en cm: '))}

accion = obstaculos(sensores)
robot['maniobra'] = accion

print('Nuevos parametros con cambio de maniobra: ')
for clave in robot:
    print(clave, ':', robot[clave])

#Pregunta de detencion de robot

pregunta = input('Desea detener el robot?: ').lower()
if pregunta == 'si':
    del  robot['Velocidad']
    robot['Estado'] = 'Estoy detenido'
    print('Nuevos valores: ')
    for clave in robot:
        print(clave, ':', robot[clave])
else:
    print('Nuevos valores: ')
    for clave in robot: 
        print(clave, ':', robot[clave])        

