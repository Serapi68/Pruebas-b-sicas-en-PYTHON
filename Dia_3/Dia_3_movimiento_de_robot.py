distancia = float(input('Digite la distancia deseada de esquive de obstaculo: '))
distancia_obs = float(input('Digite distancia de obstaculo: '))
if distancia_obs >= distancia:
    print('Detener robot')
else:
    print('Continuando ruta deseada')