bateria = float(input('Digite estado de bateria %: '))
while bateria > 0 :
    if bateria > 20 :
        bateria = bateria - 10
    else:
        bateria = bateria - 5
    print('Estado de bateria: ', bateria, '%')
    if bateria == 15:
        print ('¡SOS! bateria baja')
    elif bateria == 5:
        print('Conecta cargador o te atendras a las consecuencias')
    elif bateria == 0:
        print('Te he advertido ahora me apagare...')