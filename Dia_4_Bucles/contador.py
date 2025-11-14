limite = int(input('¿Hasta que numero quieres que cuente?: '))

contador = 0 

while contador <= limite: 
    print (contador)

    for _ in range (4):
        print('.')
    contador = contador + 1

    