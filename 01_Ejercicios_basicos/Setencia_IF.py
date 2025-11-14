temperatura = float(input('Temperatura: '))
if temperatura > 30:
    print('Esta haciendo calor ')
    print('Procura beber agua')
elif temperatura > 20: # La temperatura esta entre 20 y 302
    print('Esta haciendo un buen dia ')
elif temperatura > 10: # Depende de las otras dos 
    print('Esta haciendo frio')
else:
    print('Pues hace frio')
    