import numpy as np

sensores = np.array([33,18,20,20,30])
umbral = 25

indices_obstaculo = np.where(sensores < umbral)[0] #reconoce la posicion donde se haga verdadera la afirmacion
obstaculo = sensores[indices_obstaculo]
hay = len(obstaculo) > 0


if hay:
    
    print('Lecturas menores a ', umbral, 'cm: ', hay )
    print('¡Alerta hay un obstaculo cerca!!')
    for i in range(len(obstaculo)) :
        print('Sensor', indices_obstaculo[i] + 1, ':', obstaculo[i], 'cm' )

else:
    print('No hay moros en la costa')