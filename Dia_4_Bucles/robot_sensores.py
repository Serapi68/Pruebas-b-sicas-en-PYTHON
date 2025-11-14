Estado_Maquina = int(input('Digite encendido o apagado: ')) 
if Estado_Maquina == 0:
        print('Apagando equipo...')
elif Estado_Maquina == 1:
    Distancia = float(input('Digite distancia del obstaculo: '))
    while Estado_Maquina == 1: 
        while Distancia > 5: 
            print('Anvance normal de robot ')
            print ('Distancia de obstaculo: ', Distancia)
            Distancia = Distancia - 5          
        print ('obstaculo reconocido dictar nueva direccion')
        
        Estado_Maquina = int(input('Apagar o seguir maniobra: '))
        if Estado_Maquina == 0: 
             print ('Apagando...')
             break   
        
        Nueva_Direccion = int(input('Digite cambio derecha o izquierda:(1 = Der., 0=Izq.) '))
        if Nueva_Direccion == 1:
             print('Girando a derecha...')
        elif Nueva_Direccion == 0:
             print('Girando a izquierda...')  

        Distancia = float(input('Nueva distancia reconocida: '))
        