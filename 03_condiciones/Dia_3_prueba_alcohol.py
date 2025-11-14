edad = (int(input('¿Cual es tu edad?: ')))
permiso = (input('¿Tienes cedula? (si o no): ')) == 'si' 
if edad >= 18 and permiso == True : 
    print('tienes permiso para beber alcohol')
elif edad >= 18 and not permiso:
    print('seguramente deberias sacar tu cedula')
elif edad < 18 and permiso:
    print('Esa cedula es falsa')
else:
    print('no tienes permiso para beber')