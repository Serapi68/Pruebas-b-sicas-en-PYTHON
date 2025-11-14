posiciones = [0, 10, 20, 30, 40]  # Posiciones en cm
for pos in posiciones:
    if pos == 20:
        print('Robot en posicion: ', pos, 'cm')
        prguntar = input('¿Quieres detener el robot?: ').lower()
        if prguntar == 'si':
            print('Deteniendo robot por emergencia de distancia...')
            break
    if pos > 30:
        print('Posición', pos, 'cm: Advertencia, límite alcanzado.')
        break
    print('Robot en posición:', pos, 'cm')