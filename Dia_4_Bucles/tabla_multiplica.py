pregunta = 'si'

while pregunta.lower() == 'si':
    numero = int(input('Ingresa número para multiplicar: '))
    tipo = int(input('¿Qué resultados quieres ver? Pares = 1, Impares = 0: '))

    for i in range(1, 11):
        resultado = numero * i

        if tipo == 1 and resultado % 2 != 0:
            continue  
        elif tipo == 0 and resultado % 2 == 0:
            continue  

        
        print(numero, 'x', i, '=', resultado)

    pregunta = input('¿Quieres verificar otra tabla (si o no)? ').strip().lower()

print('¡Muchas gracias! Nos vemos pronto.')
