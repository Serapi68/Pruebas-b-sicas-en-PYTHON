nombres = ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco"]
pregunta = input('Quieres saber como se escribe tu numero?: ').lower()

while pregunta == 'si':
    try:
        numero = int(input('Digita un numero de 0 a 5: '))

        if numero >= 0  and numero <= 5:
            print( 'Tu numero', numero, ' se escribe', nombres[numero])
        else :
            print('Numero invalido')
    except ValueError:
        print('Entrada invalida, tienes que escribir un numero del 0 al 5 ')
    
    pregunta = input('¿Quieres probar otro numero?: ').lower() 

if pregunta == 'no':
    print('Fue un placer, ¡¡Hasta luego!!...') 
 