temperatura = 25
if temperatura > 30:
    print("Hace calor.")
elif temperatura > 20:
    print("Está agradable.") #Segundo chequeo de datos 
else:
    print('Hace frío')

edad = 19
tiene_permiso = False
if edad >= 18 or tiene_permiso:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")

distancia = 10  # Distancia en cm
if distancia < 20:
    print("Obstáculo cerca, detener robot.")
else:
    print("Seguir adelante.")