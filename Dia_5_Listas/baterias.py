baterias = []
for i in range(2):
    nivel = int(input("Ingresa nivel de batería " + str(i+1) + " (%): "))
    baterias.append(nivel)
promedio = sum(baterias) / len(baterias)

print("Niveles de batería:", baterias)
print("Promedio:", promedio)

while nivel > 0 :
    if nivel > 20 :
        nivel = nivel - 10
    else:
        nivel = nivel - 5
    print('Estado de bateria: ', nivel, '%')
    if nivel == 15:
        print ('¡SOS! bateria baja')
    elif nivel == 5:
        print('Conecta cargador o te atendras a las consecuencias')
    elif nivel == 0:
        print('Te he advertido ahora me apagare...')

