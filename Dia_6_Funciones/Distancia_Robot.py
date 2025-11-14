def distancia_total (pasos, longitud_paso) :
    return pasos * longitud_paso
pregunta = input('¿Desea saber la distancia total ').lower()
while pregunta == 'si':
    pasos = float(input('Ingresa numero de pasos recorridos: '))
    longitud_paso = float(input('Ingresa la longitud de cada paso en (cm): '))
    total = distancia_total(pasos, longitud_paso)
    print('Distancia total recorrida: ', total, 'cm')
    pregunta = input('¿Desea continuar el calculo de distancia?: ').lower()
print('Hemos acabado')