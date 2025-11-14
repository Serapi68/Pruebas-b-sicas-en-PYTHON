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

#Pegunta si quiere detenerse

pregunta = input('Desea detener el robot?: ').lower()
if pregunta == 'si':
    del  robot['Velocidad']
    print('Nuevos valores: ')
    for clave in robot:
        print(clave, ':', robot[clave])
else:
    print('Nuevos valores: ')
    for clave in robot: 
        print(clave, ':', robot[clave])        
