import time


Peso = input('Inserta tu peso actual: ')
tipo_peso = input ('Que tipo de unidad tienes de peso (K)g o (L)bs: ').upper()


if tipo_peso == 'K' :
    peso_libra = float(Peso) * 2.2046
    print('Tu peso en libras es : ' + str(peso_libra ))
if tipo_peso == 'L':
    peso_kilo = float(Peso) * 0.45359237
    print('Tu peso en kilos es : ' + str (peso_kilo))
else: 
    ('No has insertado dato valido')
time.sleep(5)