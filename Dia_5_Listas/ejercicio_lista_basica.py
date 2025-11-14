nombres = ['Sergio', 'Gabriela', 'Juan', 'David', 'Santiago']
print('Lista de nombres:', nombres)

pregunta = input('¿Quieres añadir un nuevo nombre? ').lower()

if pregunta == 'si':
    while pregunta == 'si':
        nuevo_nombre = input('Digite nuevo nombre al final de la lista: ').capitalize()
        
        if nuevo_nombre in nombres:
            print('El nombre',  nuevo_nombre,  'ya está en la lista.')
        else:
            nombres.append(nuevo_nombre)
            print('Nombre agregado con éxito.')
        
            print('Lista actualizada:', nombres)
        corregir_añadidura = input('¿Quieres eliminar el nombre añadido?: ').lower()
        if corregir_añadidura == 'si':
            nombres.pop()
            print('se ha restablecido la lista: ', nombres)
        pregunta = input('¿Tienes otro nombre para añadir?: ').lower()


modificar_posicion = input('¿Quieres modificar de posicion algun nombre?: ').lower()
if modificar_posicion == 'si':
    print(nombres)
    while modificar_posicion == 'si' :
        posicion = (input('Digite el nombre a mover: ')).capitalize()
        if posicion in nombres: 
            nueva_posicion = int(input('A que posicion quieres cambiar el nombre: '))
            if 0 <= nueva_posicion < len(nombres):
                nombres.remove(posicion)
                nombres.insert(nueva_posicion, posicion)
                print(nombres)
            else:
                print('Posicion invalida ')
        else:
            print('El nombre ', posicion, 'no esta en la lista')
        modificar_posicion = input( '¿Quieres seguir modificando?: ' ).lower()

eliminar_posicion = input('¿Quieres eliminar algun nombre de la lista?: ').lower()
if eliminar_posicion == 'si':
    print(nombres)
    while eliminar_posicion == 'si':
        eliminar = input('Digite el nombre a eliminar: ').capitalize()
        if eliminar in nombres:
            nombres.remove(eliminar)
            print('Nueva lista: ', nombres)
        else:
            print('Este nombre no esta en la lista')
        eliminar_posicion = input('Quieres eliminar otro nombre: ').lower()

print('Muchas gracias ya se han hecho las modificaciones requeridas!!!')
print(nombres)